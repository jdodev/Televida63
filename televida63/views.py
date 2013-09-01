from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from televida63.forms import ContactoForm
from django.utils import simplejson
from televida63.models import *
from datetime import datetime
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage

def inicio(request2televida):
	UltNoticias = Noticia.objects.all()[:5]
	AllBanners = Banners.objects.all().order_by('OrdenBanner')[:8]
	return render_to_response('index.html', {'TNoticias' : UltNoticias, 'TBanners' : AllBanners}, context_instance=RequestContext(request2televida))

def VerNoticia(request, IdNoticia):
	dato = get_object_or_404(Noticia, pk=IdNoticia)
	NoticiaFiltrada = Noticia.objects.filter(id=IdNoticia)
	return render_to_response('verNoticia.html', {'Filtrada' : dato}, context_instance=RequestContext(request))

def VerNoticiasTodos(request):
	AllNoticias = Noticia.objects.all().order_by('id')
	pagina = Paginator(AllNoticias, 25)

	page = request.GET.get('page')
	try:
		Noticias2 = pagina.page(page)
	except PageNotAnInteger:
		Noticias2 = pagina.page(1)
	except EmptyPage:
		Noticias2 = pagina.page(pagina.num_pages)

	return render_to_response('listNoticias.html', {'TNoticias' : Noticias2}, context_instance=RequestContext(request))

def ListaBlogs(request):
	AllPeriodistas = Periodista.objects.all().order_by('NombrePeriodista')
	return render_to_response('listBlogs.html', {'TPeriodistas' : AllPeriodistas}, context_instance=RequestContext(request))

def VerEntradasBlog(request, IdBlogP):
	EntradasPeriodista = BlogEntrada.objects.filter(IdPeriodista=IdBlogP).order_by('-FechaPublicacion')[:10]
	return render_to_response('verBlog.html', {'BlogEntradas' : EntradasPeriodista}, context_instance=RequestContext(request))


def contacto(request):
	if request.method=='POST':
		formulario = ContactoForm(request.POST)
		if formulario.is_valid():
			titulo = 'Mensaje desde el sitio web de Televida'
			contenido = 'De: ' + formulario.cleaned_data['NombreCompleto'] + '\n'
			contenido += 'Email: ' + formulario.cleaned_data['Correo'] + '\n'
			contenido += formulario.cleaned_data['Mensaje']
			correo = EmailMessage(titulo, contenido, to=['jdoavila@gmail.com'])
			correo.send()
			return HttpResponseRedirect('/')
	else:
		formulario = ContactoForm()
	return render_to_response('contacto.html', {'formi' : formulario}, context_instance=RequestContext(request))