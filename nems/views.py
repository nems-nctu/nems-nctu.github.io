from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls.static import static
from nems.settings import *

import json

# pattern
path_pattern = STATICFILES_DIRS[0] + '/data/{}.json'

def home(request):
	return render(request, 'home.html')

def projects(request):
	with open(path_pattern.format('projects'), 'r') as file:
		projects = json.load(file)
	return render(
		request, 
		'projects.html',
		{ 'projects': projects }
	)

def publications(request):
	return render(request, 'publications.html')

def people(request):
	with open(path_pattern.format('people'), 'r') as file:
		people = json.load(file)
	return render(
		request, 
		'people.html', 
		{'people': people}
	)

def links(request):
	return render(request, 'links.html')

def gallery(request):
	with open(path_pattern.format('gallery'), 'r') as file:
		gallery = json.load(file)
	return render(
		request, 
		'gallery.html', 
		{ 'gallery': gallery }
	)

def download(request):
	return render(request, 'download.html')

def demo(request):
	return render(request, 'demo.html')

def custom_404(request):
	print('erer')
	return HttpResponseNotFound('<h1>Page not found</h1>')