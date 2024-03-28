import os
import re
import urllib
import requests

from bs4 import BeautifulSoup

from django.core.management.base import BaseCommand


def extract_text(soup):
    texto = ""
    for line in soup.find_all("div", {"class": [ "content-text", "text", "text   ", "post-item-wrap"]}):
        if line.text:
            texto += line.text + '\n'

    for line in soup.find_all("section", {"class": ["internalContent"]}):
        if line.text:
            texto += line.text

    if not texto:
        for article in soup.find_all("article"):
            for lines in article.find_all("div"):
                line = re.sub("\s+", " ", lines.text).strip()
                if line:
                    texto += line + '\n'

    if not texto:
        texto = soup.get_text()

    lines = (line.strip() for line in texto.splitlines())
    # break multi-headlines into a line each
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    # drop blank lines
    texto = '\n'.join(chunk for chunk in chunks if chunk)

    return texto


class Command(BaseCommand):
    help = 'Remoção automatizada dos textos'

    def add_arguments(self, parser):
        parser.add_argument('-u', '--url', type=str, help='URL')

    def handle(self, *args, **options):
        base_dir = os.path.dirname(os.path.abspath(__file__)).split('/')[:-3]
        base_dir = '/'.join(base_dir)
        url_base = options['url']
        pdf_path = os.path.join('/', base_dir, 'media', 'uploads')
        print('Path de upload: %s' % pdf_path)
        headers = {'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.146 Safari/537.36',
                   'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                   "X-Amzn-Trace-Id": "Root=%s" % hex(1111)
                   }
        response = requests.get(url_base, headers=headers)
        soup = BeautifulSoup(response.content, features="html.parser")
        for script in soup([ "script", "style", "noscript" ]):
            script.extract()  # rip it out all scripts and styles
        paginas = []
        for pagina in soup.find_all('a'):
            paginas.append(pagina['href'])

        tot_files = 0
        tot_links = 0
        for pagina in paginas:
            url = f'{url_base}{pagina}'
            print(f'Página {url}')
            response = requests.get(url, headers=headers)
            soup = BeautifulSoup(response.content, features="html.parser")
            filename = os.path.join(pdf_path, pagina)
            with open(filename, 'wb') as f:
                f.write(response.content)
            for tag in soup.find('div', {'id': 'conteúdo'}).find_all('a'):
                link = tag['href']
                if link[-4:] == '.pdf':
                    url_arquivo = link
                    url_arquivo = url_arquivo.replace('../','')
                    response = requests.get(f'{url_base}{url_arquivo}', headers=headers)
                    if response.status_code == 200:
                        full_path = os.path.join(pdf_path, url_arquivo.split('/pdfs/')[-1])
                        full_path = urllib.parse.unquote(full_path, 'latin')
                        path = os.path.dirname(full_path)
                        os.makedirs(path, mode=0o751, exist_ok=True)
                        if os.path.exists(full_path):
                            print(f'Arquivo já existia {full_path}')
                        else:
                            with open(full_path, 'wb') as f:
                                f.write(response.content)
                    else:
                        print(f'Arquivo não encontrado {url_arquivo}')
                    tot_files += 1
                else:
                    tot_links += 1

        print(f'Total de arquivos importados: {tot_files}')
        print(f'Total de links: {tot_links}')
