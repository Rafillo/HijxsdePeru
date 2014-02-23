from website.models import *
from django.contrib import admin
from markitup.widgets import AdminMarkItUpWidget

admin.site.register(Pagina)
admin.site.register(Tema)
admin.site.register(TipoAutor)
admin.site.register(Autor)
admin.site.register(Comentario)
admin.site.register(Doc)
admin.site.register(Noticia)
admin.site.register(Enlace)
admin.site.register(Galeria)
admin.site.register(Foto)
admin.site.register(Agenda)
admin.site.register(Blog)
admin.site.register(Presx)

#class BlogAdmin(admin.ModelAdmin):
#    formfield_overrides = {models.TextField: {'widget': AdminMarkItUpWidget}}

#admin.site.register(Blog, BlogAdmin)
