from django.http import Http404
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, get_object_or_404
# Create your views here.
def basepage(request):
	template=loader.get_template('gstic/basepage.html')
	return(HttpResponse(template.render({},request)))
	
def StartSearch(request):
	template=loader.get_template('gstic/StartSearch.html')
	return(HttpResponse(template.render({},request)))