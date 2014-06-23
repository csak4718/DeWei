# views.py is controller
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext, loader

# Create your views here.
def index(request):
	return HttpResponse('Hello World. You are at dwkung index')#view