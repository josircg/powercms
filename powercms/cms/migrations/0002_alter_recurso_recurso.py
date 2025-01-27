# Generated by Django 3.2.22 on 2023-10-24 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='recurso',
            field=models.CharField(choices=[('EMAIL', 'Envio de email automático'), ('SITE_NAME', 'Nome do Site'), ('ROBOTS', 'Permite busca pelo Google'), ('COMMENT_P', 'Texto para comentários privados'), ('COMMENT', 'Texto para comentários'), ('SIGNUP', 'Permite cadastro de usuários'), ('EMAILADMIN', 'Quem recebe avisos de novos usuários'), ('ANALYTICS', 'Google Analytics'), ('CAPTCHA_PU', 'RECAPTCHA_PUBLIC_KEY'), ('CAPTCHA_PR', 'RECAPTCHA_PRIVATE_KEY'), ('OG-IMAGE', 'Imagem default para redes sociais'), ('TAGS', 'Nuvem de Tags'), ('TAGS-EXC', 'Excluir tags da núvem de tags (separar por virgula)'), ('TAGS-FIXA', 'Tags Fixas (separar por virgula)'), ('FACEBOOK', 'Facebook app id'), ('SUP_SLUG', 'Código no supervisord')], max_length=10, unique=True, verbose_name='Parâmetro'),
        ),
    ]
