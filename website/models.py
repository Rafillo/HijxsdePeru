# -*- coding: utf-8 -*-

#import os

from django.db import models
from django.core.urlresolvers import reverse
from django.template.defaultfilters import slugify

from taggit.managers import TaggableManager
from tinymce import models as tinymce_models

class Pagina(models.Model):
    idpagina = models.AutoField(primary_key=True, verbose_name="Id")
    pagina = models.CharField(max_length=500, verbose_name="Titulo")
    foto = models.ImageField(null=True, blank=True, upload_to='pagina', verbose_name="Foto")
    descripcion = tinymce_models.HTMLField(verbose_name="Descripcion")
    class Meta:
        db_table = 'pagina'
        verbose_name = 'Pagina'
        ordering = ['-idpagina']

    def __unicode__(self):
        return self.pagina


class Tema(models.Model):
    idtema = models.AutoField(primary_key=True, verbose_name="Id")
    tema = models.CharField(max_length=500, verbose_name="Titulo")
    class Meta:
        db_table = 'tema'
        verbose_name = 'Tema'
        ordering = ['-idtema']

    def __unicode__(self):
        return self.tema


class TipoAutor(models.Model):
    idtipo_autor = models.AutoField(primary_key=True, verbose_name="Id")
    tipo_autor = models.CharField(max_length=500, verbose_name="Tipo Autor")
    class Meta:
        db_table = 'tipo_autor'
        verbose_name = 'Tipo de Autor'
        ordering = ['-idtipo_autor']

    def __unicode__(self):
        return self.tipo_autor


class Autor(models.Model):
    idautor = models.AutoField(primary_key=True, verbose_name="Id")
    autor = models.CharField(max_length=500, verbose_name="Autor")
    email = models.EmailField(null=True, blank=True, max_length=150, verbose_name="E-mail")
    foto = models.ImageField(null=True, blank=True, upload_to='autor', verbose_name="Foto")
    tipo_autor = models.ForeignKey(TipoAutor, db_column="idtipo_autor", verbose_name="TipoAutor", null=True, blank=True)
    class Meta:
        db_table = 'autor'
        verbose_name = 'Autor'
        ordering = ['idautor']

    def __unicode__(self):
        return self.autor

class Doc(models.Model):
    iddoc = models.AutoField(primary_key=True, verbose_name="Id")
    doc = models.CharField(max_length=500, verbose_name="Titulo")
    fecha = models.DateField(null=True, blank=True, verbose_name="Fecha")
    portada = models.ImageField(null=True, blank=True, upload_to='doc', verbose_name="Imagen")
    descripcion = tinymce_models.HTMLField(null=True, blank=True, verbose_name="Descripcion")
    archivo = models.FileField(null=True, blank=True, upload_to='doc', verbose_name="Archivo")
    tags = TaggableManager(blank=True)

    def get_absolute_url(self):
        return reverse('doc_detail',
            kwargs={
            'pk': self.pk,
            'slug': slugify(self.doc)[:60],
            })

    class Meta:
        db_table = 'doc'
        verbose_name = 'Documento'
        ordering = ['-fecha','-iddoc']

    def __unicode__(self):
        return self.doc


class Noticia(models.Model):
    noticia = models.CharField(null=True, blank=True, max_length=500, verbose_name="Titulo")
    fecha = models.DateField(null=True, blank=True, verbose_name="Fecha")
    texto = tinymce_models.HTMLField(null=True, blank=True, verbose_name="Texto")
    url = models.CharField(null=True, blank=True, max_length=1000, verbose_name="URL")
    foto = models.ImageField(null=True, blank=True, upload_to='noticia', verbose_name="Foto")
    tags = TaggableManager(blank=True)

    def get_absolute_url(self):
        return reverse('noticia_detail',
            kwargs={
            'pk': self.pk,
            'slug': slugify(self.noticia)[:60],
            })

    class Meta:
        db_table = 'noticia'
        verbose_name = 'Noticia'
        ordering = ['-fecha']

    def __unicode__(self):
        return self.noticia


class Enlace(models.Model):
    idenlace = models.AutoField(primary_key=True, verbose_name="Id")
    enlace = models.CharField(max_length=500, verbose_name="Título")
    url = models.URLField(max_length=600, verbose_name="Dirección web")
    texto = models.TextField(null=True, blank=True, verbose_name="Texto")
    imagen = models.ImageField(null=True, blank=True, upload_to='enlace', verbose_name="Imagen")
    class Meta:
        db_table = 'enlace'
        verbose_name = 'Enlace'
        ordering = ['-idenlace']

    def __unicode__(self):
        return self.enlace


class Galeria(models.Model):
    idgaleria = models.AutoField(primary_key=True, verbose_name="Id")
    galeria = models.CharField(max_length=500, verbose_name="Titulo")
    fecha = models.DateField(null=True, blank=True, verbose_name="Fecha")
    class Meta:
        db_table = 'galeria'
        verbose_name = 'Galeria'
        ordering = ['-idgaleria']

    def __unicode__(self):
        return self.galeria


class Foto(models.Model):
    idfoto = models.AutoField(primary_key=True, verbose_name="Id")
    galeria = models.ForeignKey(Galeria, db_column="idgaleria", verbose_name="Galeria")
    foto = models.CharField(null=True, blank=True, max_length=500, verbose_name="Titulo")
    imagen = models.ImageField(null=True, blank=True, upload_to='foto', verbose_name="Foto")
    class Meta:
        db_table = 'foto'
        verbose_name = 'Foto'
        ordering = ['-galeria','-idfoto']

    def __unicode__(self):
        return self.foto


class Blog(models.Model):
    blog = models.CharField(max_length=500, verbose_name="Titulo")
    autor = models.ForeignKey(Autor, null=True, blank=True, db_column="idautor", verbose_name="Autor")
    tipoautor = models.ForeignKey(TipoAutor, null=True, blank=True, db_column="idtipo_autor", verbose_name="Tipo Autor")
    fecha = models.DateField(null=True, blank=True, verbose_name="Fecha")
    resumen = tinymce_models.HTMLField(null=True, blank=True, verbose_name="Resumen")
    texto = tinymce_models.HTMLField(null=True, blank=True, verbose_name="Descripcion")
    imagen = models.ImageField(upload_to='blog',  null=True, blank=True, verbose_name="Imagen 1")
    video = models.URLField(null=True, blank=True, verbose_name="Video 1")
    tema = models.ForeignKey(Tema, db_column="idtema", null=True, blank=True, verbose_name="Tema")
    galeria = models.ForeignKey(Galeria, null=True, blank=True, verbose_name="Galería")
    portada = models.BooleanField(blank=True, verbose_name="Portada?")
    tags = TaggableManager(blank=True)

    #def save(self, *args, **kwargs):
    #    if not self.slug:
    #        self.slug = slugify(self.blog)[:60]
    #
    #    super(News, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog_detail',
            kwargs={
            'pk': self.pk,
            'slug': slugify(self.blog)[:60],
            })

    class Meta:
        db_table = 'blog'
        verbose_name = 'Blog'
        ordering = ['-fecha']

    def __unicode__(self):
        return self.blog

class Agenda(models.Model):
    idagenda = models.AutoField(primary_key=True, verbose_name="Id")
    agenda = models.CharField(max_length=500, verbose_name="Titulo")
    fecha = models.DateField(null=True, blank=True, verbose_name="Fecha")
    lugar = models.CharField(null=True, blank=True, max_length=120, verbose_name="Lugar")
    texto = models.TextField(null=True, blank=True, verbose_name="Evento")
    organiza = models.CharField(null=True, blank=True, max_length=500, verbose_name="Organizado por")
    class Meta:
        db_table = 'agenda'
        verbose_name = 'Agenda'
        ordering = ['-fecha']

    def __unicode__(self):
        return self.agenda

class Comentario(models.Model):
    idcomentario = models.AutoField(primary_key=True, verbose_name="Id")
    blog = models.ForeignKey(Blog, db_column="idblog", verbose_name="Blog")
    nombre = models.CharField(max_length=80, verbose_name="Nombre")
    comentario = models.TextField(verbose_name="Comentario")
    email = models.EmailField(max_length=80, verbose_name="Email")
    publicado = models.BooleanField(verbose_name="Publicado")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha")
    ip = models.IPAddressField(max_length=15, verbose_name="Ip")
    class Meta:
        db_table = 'comentario'
        verbose_name = 'Comentario'
        ordering = ['-idcomentario']

    def __unicode__(self):
        return self.comentario


class Perfil(models.Model):
    nombre = models.CharField(max_length=500)
    slug = models.SlugField(max_length=100, unique=True)
    foto = models.ImageField(null=True, blank=True, upload_to='autor', verbose_name="Foto")
    bio = tinymce_models.HTMLField(verbose_name="Descripción")

    class Meta:
        ordering = ['nombre']

    def __unicode__(self):
        return self.nombre

    def save(self):
        self.slug = slugify(self.nombre)
        super(Perfil, self).save()
