#import mongoengine
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Message

#user = authenticate(username='', password='')
#assert isinstance(user, mongoengine.django.auth.User)

def Contact(request):
    template = loader.get_template('Introduction/Contact.html')
    context = "Hello, world. You are at the Message index."
    return HttpResponse(template.render(context))

def About(request):
    template = loader.get_template('Introduction/About.html')
    context = "Welcome to Pure Investments"
    return HttpResponse(template.render(context))

def Demo(request):
    template = loader.get_template('Introduction/Demo.html')
    context = "Welcome to Pure Investments"
    return HttpResponse(template.render(context))

