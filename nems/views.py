from django.shortcuts import render
from django.http import HttpResponse
from django.conf.urls.static import static

def index(request):
	return render(request, 'index.html')

def projects(request):
	# var
	projects = [
		{
			'title': 'Customizable WiFi',
			'image': {
				'path': 'img/project_wifi.jpg',
				'width': 300
			},
			'content': 'As the Wi-Fi technology becomes pervasive in reality, its usage pattern is also turning highly diversified in operation settings and application scenarios. This leads to new design requirements for Wi-Fi networking solutions in terms of various combinations in throughput, latency and energy efficiency. We believe that both the user demand pull and the technology push call for customizable Wi-Fi solutions.'
		},
		{
			'title': 'Mobile Security',
			'image': {
				'path': 'img/project_security.jpg',
				'width': 300
			},
			'content': 'To support various advanced services, the mobile Internet technology is evolving from a simple, working design to a resilient, high-performance networking solution suite. For example, during the evolution from 2G/3G to 4G, the security impact is not fully understood. My research shows that unprecedented malicious attacks can be launched on both mobile devices and the network infrastructure in 3G/4G systems. It is because security loopholes usually lie in the newly offered services (e.g., IoT and D2D) or those legacy ones (e.g., VoLTE) that require new interactions.'
		},
		{
			'title': 'Integrated WiFi/WiGig Networking',
			'image': {
				'path': 'img/project.png',
				'width': 30
			},
			'content': 'To be updated ...'
		},
		{
			'title': 'V2X Networked System',
			'image': {
				'path': 'img/project.png',
				'width': 30
			},
			'content': 'To be updated ...'
		},
		{
			'title': '5G Mobile Edge Computing',
			'image': {
				'path': 'img/project.png',
				'width': 30
			},
			'content': 'To be updated ...'
		}
	]
	return render(
		request, 
		'projects.html',
		{ 'projects': projects }
	)

def publications(request):
	return render(request, 'publications.html')

def people(request):
	# var
	people = {
		'faculty': [
			{
				'name': {
					'en': 'Chi-Yu Li',
					'cht': '李奇育'
				},
				'image': 'img/people/chiyuli.jpg',
				'url': 'http://people.cs.nctu.edu.tw/~chiyuli/index.html'
			}
		],
		'phd': [
			{
				'name': {
					'en': '',
					'cht': ''
				},
				'image': 'img/people/hiring.jpg',
				'url': ''
			}
		],
		'assistant': [
			{
				'name': {
					'en': '',
					'cht': ''
				},
				'image': 'img/people/hiring.jpg',
				'url': ''
			}
		],
		'2016': [
			{
				'name': {
					'en': 'Chien-Ting Kuo',
					'cht': '郭建廷'
				},
				'image': 'img/people/ctkuo.jpg',
				'url': ''
			},
			{
				'name': {
					'en': 'Chia-Jui Yeh',
					'cht': '葉家睿'
				},
				'image': 'img/people/cjyeh.jpg',
				'url': ''
			},
			{
				'name': {
					'en': 'Yao-Yu Li',
					'cht': '李曜宇'
				},
				'image': 'img/people/yaoyuli.jpg',
				'url': ''
			},
			{
				'name': {
					'en': 'Giovanni Salinas',
					'cht': '羅吉凡'
				},
				'image': 'img/people/gio.jpg',
				'url': ''
			}
		],
		'2017': [
			{
				'name': {
					'en': 'Syuan-Cheng Chen',
					'cht': '陳軒丞'
				},
				'image': 'img/people/scchen.jpg',
				'url': ''
			},
			{
				'name': {
					'en': 'Yu-Han Lu',
					'cht': '呂昱翰'
				},
				'image': 'img/people/yuhanlu.jpg',
				'url': ''
			},
			{
				'name': {
					'en': 'Louie Lu',
					'cht': '呂紹榕'
				},
				'image': 'img/people/male.jpg',
				'url': ''
			},
			{
				'name': {
					'en': 'Pei-Yuan Hong',
					'cht': '洪培元'
				},
				'image': 'img/people/male.jpg',
				'url': ''
			},
			{
				'name': {
					'en': '',
					'cht': ''
				},
				'image': 'img/people/hiring.jpg',
				'url': ''
			}
		],
		'alumni': [
			{
				'name': {
					'en': 'Wei-Han Chen',
					'cht': 'Phd in OSU'
				},
				'image': 'img/people/whchen.jpg',
				'url': ''
			}
		],
	}
	return render(request, 'people.html', {'people': people})

def links(request):
	return render(request, 'links.html')

def gallery(request):
	# var
	photos = [
		{
			'url': 'img/gallery/20170728.jpg',
			'alt': 'Lab'
		},
		{
			'url': 'img/gallery/20170615.jpg',
			'alt': 'Lab dinner'
		},
		{
			'url': 'img/gallery/20170606.jpg',
			'alt': 'Jamie'
		}
	]
	return render(request, 'gallery.html', { 'photos': photos })

def download(request):
	return render(request, 'download.html')

def demo(request):
	return render(request, 'demo.html')

