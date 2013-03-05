from website.models import *
from django.contrib import admin
from markitup.widgets import AdminMarkItUpWidget

admin.site.register(pagina)
admin.site.register(tema)
admin.site.register(tipo_autor)
admin.site.register(autor)
admin.site.register(comentario)
admin.site.register(doc)
admin.site.register(noticia)
admin.site.register(enlace)
admin.site.register(galeria)
admin.site.register(foto)
admin.site.register(agenda)

class BlogAdmin(admin.ModelAdmin):
    formfield_overrides = {models.TextField: {'widget': AdminMarkItUpWidget}}

admin.site.register(Blog, BlogAdmin)
