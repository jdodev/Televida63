#encoding:utf-8
from django.forms import ModelForm
from django import forms

class ContactoForm(forms.Form):
	NombreCompleto = forms.CharField(max_length=100, label='Nombre:', required=True, help_text='Nombre Completo')
	Correo = forms.EmailField(label='Email', required=True, help_text='Correo Electrónico')
	Mensaje = forms.CharField(widget=forms.Textarea, label='Mensaje', required=True, help_text='Mensaje a enviar.')