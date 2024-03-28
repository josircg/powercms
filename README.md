
# PowerCMS 1.7

![Python version](https://img.shields.io/badge/python-3.6%7C3.7%7C3.8%7C3.9%7C3.10-blue)
![Django version](https://img.shields.io/badge/django-3.2-yellow)

O PowerCMS é um Content Management System (CMS) feito em Django. Tem como objetivo permitir que um usuário que não seja programador/designer possa atualizar um site ou blog sem a intervenção de um profissional de TI.

Entra na mesma categoria de softwares como o Wordpress, Blogspot mas é ideal para pessoas **não** precisam de todas as funcionalidades destes pacotes complexos.

* Mais rápido
* Mais simples
* Mais seguro (por não permitir plugins inseguros, principal motivo de invasões)
* Ferramentas de SEO
* Proteção do site contra buscas (para sites privados)
* Hotlinks para medição de campanhas

Ele permite o uso de temas e contém funcionalidades como backup e restore da base, gerenciamento de álbuns de imagens e várias outras funcionalidades.

Pontos negativos:

* Interface bem mais simples;
* Número pequeno de temas disponíveis para uso;
* Desenvolvimento de novos temas deve ser feito por profissionais que conheçam Django;

Aceita integração com o PowerPanel (equivalente ao CPanel) também em Django para permitir que o usuário possa criar vários sites em um mesmo servidor. 
Entretanto, não requer que esta ferramenta esteja instalada.

## Sobre as versões:
 - Essa versão não deve ser utilizada para atualizar um site com versão menor que a 1.6
    
## Para migração de um site em uma versão anterior a 1.7:
 - Criar uma nova instalação com a versão 1.7
 - Importar o tema, colocando o mesmo nome do tema do site antigo
 - Importar os artigos a partir do backup gerado via python manage.py backup_artigos
 - Importar a pasta media