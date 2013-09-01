from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
#from emet.forms import ActasPresidentesForm, ActasDiputadosForm, ActasAlcaldesForm
from django.utils import simplejson
from televida63.models import *
from datetime import datetime
from django.core import serializers
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def inicio(request):
	UltNoticias = Noticia.objects.all()[:5]
	AllBanners = Banners.objects.all().order_by('OrdenBanner')[:8]
	return render_to_response('index.html', {'TNoticias' : UltNoticias, 'TBanners' : AllBanners}, context_instance=RequestContext(request))

def VerNoticia(request, IdNoticia):
	dato = get_object_or_404(Noticia, pk=IdNoticia)
	NoticiaFiltrada = Noticia.objects.filter(id=IdNoticia)
	return render_to_response('verNoticia.html', {'Filtrada' : dato}, context_instance=RequestContext(request))

def VerNoticiasTodos(request):
	AllNoticias = Noticia.objects.all().order_by('id')
	pagina = Paginator(AllNoticias, 2)

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