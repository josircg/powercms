from django import forms

from cms.email import sendmail
from cms.models import Recurso


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    email = forms.EmailField(label='Email')
    telefone = forms.CharField(label='Telefone', max_length=13, required=False)
    cidade = forms.CharField(label='Cidade', max_length=100, required=False)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea)

    def sendemail(self):
        email_admin = Recurso.objects.get_or_create(recurso=u'EMAILADMIN')[0]
        if email_admin.valor:
            mensagem = (
                '<h1>Novo Contato</h1>'
                '<p><b>Nome:</b> {nome}</p>'
                '<p><b>Email:</b> {email}</p>'
                '<p><b>Telefone:</b> {telefone}</p>'
                '<p><b>Cidade:</b> {cidade}</p>'
                '<p><b>Mensagem:</b> {mensagem}</p>'
            ).format(
                nome=self.cleaned_data.get('nome'), email=self.cleaned_data.get('email'),
                telefone=self.cleaned_data.get('telefone'), cidade=self.cleaned_data.get('cidade'),
                mensagem=self.cleaned_data.get('mensagem'),
            )
            sendmail(
                subject='{site} - Novo contato'.format(site=Recurso.objects.get(recurso='SITE_NAME').valor),
                to=email_admin.valor.split('\n'),
                template=mensagem,
                headers={'Reply-To': self.cleaned_data.get('email')}
            )
