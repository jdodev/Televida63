from televida63.models import *
from django.contrib import admin

class Editorcito(admin.ModelAdmin):
	class Media:
		js = ('../static/js/tiny_mce/tiny_mce.js',
			'../static/js/editores/textareas.js')

admin.site.register(Periodista)
admin.site.register(TiposNoticia)
admin.site.register(Noticia, Editorcito)
admin.site.register(Programa)
admin.site.register(Programacion)
admin.site.register(Banners)
admin.site.register(BlogEntrada, Editorcito)
admin.site.register(Reproductor)