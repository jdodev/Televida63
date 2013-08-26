from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
#from emet.forms import ActasPresidentesForm, ActasDiputadosForm, ActasAlcaldesForm
from django.utils import simplejson
#from emet.models import RepPresidentes, Movimientos, ActasPresidentes, ActasAlcaldes, RepAlcaldes, RepDiputados, ActasDiputados
from datetime import datetime
from django.core import serializers

def inicio(request):
	#formulario = AuthenticationForm()
	#return render_to_response('home.html', {'formulario':formulario}, context_instance=RequestContext(request))
	html = "<html><body>televida63.com</body></html>"
	return HttpResponse(html)