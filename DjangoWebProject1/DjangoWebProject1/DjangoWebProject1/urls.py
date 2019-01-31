"""
Definition of urls for DjangoWebProject1.
"""

from django.conf.urls import include, url
from DjangoWebProject1 import contact
from DjangoWebProject1.contact import views


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [
	url(r'^$', contact.views.index, name='index'),
    url(r'^home$', contact.views.index, name='home'),
    # Examples:
    # url(r'^$', DjangoWebProject1.views.home, name='home'),
    # url(r'^DjangoWebProject1/', include('DjangoWebProject1.DjangoWebProject1.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
]
