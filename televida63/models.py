#encoding:utf-8
from django.db import models

class Periodista(models.Model):
	NombrePeriodista = models.CharField(max_length=100, help_text='Nombres del Periodista', verbose_name=u'Nombres')
	ApellidoPeriodista = models.CharField(max_length=100, help_text='Apellidos del Periodista', verbose_name=u'Apellidos')
	FotoPeriodista = models.ImageField(upload_to='periodistas', verbose_name=u'Foto')
	BiografiaPeriodista = models.TextField(max_length=10000, help_text='Biografía del Periodista', verbose_name=u'Biografía')

	def __unicode__(self):
		return self.NombrePeriodista

class TiposNoticia(models.Model):
	TipoNoticia = models.CharField(max_length=50, help_text='Tipo de Noticia', verbose_name=u'Tipo Noticia')

	def __unicode__(self):
		return self.TipoNoticia

class Noticia(models.Model):
	TituloNoticia = models.CharField(max_length=100, help_text='Titulo de la Noticia', verbose_name=u'Titulo')
	TextoNoticia = models.TextField(help_text='Redacción de la Noticia', verbose_name=u'Noticia')
	ImagenNoticia = models.ImageField(upload_to='noticias', verbose_name=u'Imagen')
	IdTipoNoticia = models.ForeignKey(TiposNoticia)
	IdPeriodista = models.ForeignKey(Periodista)
	FechaNoticia = models.DateTimeField(auto_now_add=True, help_text='Fecha de la Noticia', verbose_name=u'Fecha')

	def __unicode__(self):
		return self.TituloNoticia

class Programa(models.Model):
	TituloPrograma = models.CharField(max_length=100, help_text='Titulo del Programa', verbose_name=u'Titulo')
	DescripcionPrograma = models.TextField(help_text='Descripción del Programa', verbose_name=u'Descripción')
	ImagenPrograma = models.ImageField(upload_to='programas', verbose_name=u'Programas')

class Programacion(models.Model):
	IdPrograma = models.ForeignKey(Programa)
	Lunes = models.BooleanField(verbose_name=u'Lunes')
	Martes = models.BooleanField(verbose_name=u'Martes')
	Miercoles = models.BooleanField(verbose_name=u'Miércoles')
	Jueves = models.BooleanField(verbose_name=u'Jueves')
	Viernes = models.BooleanField(verbose_name=u'Viernes')
	Sabado = models.BooleanField(verbose_name=u'Sábado')
	Domingo = models.BooleanField(verbose_name=u'Domingo')
	HoraInicio = models.TimeField(auto_now=False, auto_now_add=False, verbose_name=u'Hora Inicio')
	HoraFin = models.TimeField(auto_now=False, auto_now_add=False, verbose_name=u'Hora Fin')

	def __unicode__(self):
		return self.IdPrograma

class Banners(models.Model):
	TituloBanner = models.CharField(max_length=100, help_text='Titulo del Banner', verbose_name=u'Titulo')
	ImagenBanner = models.ImageField(upload_to='banners', verbose_name=u'Imagen')
	OrdenBanner = models.IntegerField(help_text='Orden del Banner', verbose_name=u'Orden')
	UrlBanner = models.URLField(help_text='Enlace a...', verbose_name=u'Enlace', blank=True, null=True)

	def __unicode__(self):
		return self.TituloBanner

