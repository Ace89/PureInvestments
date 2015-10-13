from django.conf.urls import url

from . import views

urlpatterns = [
	# ex: /Introduction/
	url(r'^$', views.About, name='About'),
	url(r'^Contact/$', views.Contact, name='Contact'),
	url(r'^Demo/$', views.Demo, name='Demo'),
]
