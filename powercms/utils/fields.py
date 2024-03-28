# coding:utf-8
from django.db import models
from utils.forms import BRDateFormField, BRDecimalFormField

from django.forms.fields import Field
from django.core.serializers.json import DjangoJSONEncoder
import ast, json, os, uuid


def formata_nome_do_arquivo(objeto, nome_arquivo):
    nome, extensao = os.path.splitext(nome_arquivo)
    return os.path.join('imagens', str(uuid.uuid4()) + extensao.lower())


class BRDateField(models.DateField):
    def formfield(self, **kwargs):
        kwargs.update({'form_class': BRDateFormField})
        return super(BRDateField, self).formfield(**kwargs)


class BRDecimalField(models.DecimalField):
    def formfield(self, **kwargs):
        kwargs.update({'form_class': BRDecimalFormField})
        return super(BRDecimalField, self).formfield(**kwargs)

