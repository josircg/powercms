# coding: utf-8
from django.conf.urls import  include, url
# from views import *
from django.urls import re_path

from crm.views import ContatoView

urlpatterns = [
    re_path(r'^contato/$', ContatoView.as_view(), name='contato'),
    re_path(r'^cadastro/$', ContatoView.as_view(), name='cadastro'),
]
