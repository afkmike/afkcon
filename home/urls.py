__author__ = 'Mark'
from django.conf.urls import patterns, url
from home import views as v

urlpatterns = patterns('',
        url(r'^$', v.index, name='home'),
        url(r'^home.htm', v.index, name='home'),
        url(r'^contact.htm', v.contact, name='contact'),
        url(r'^services.htm', v.services, name='services'),
        )