# -*- coding: utf-8 -*-

from django.db import models

class pagina(models.Model):
    idpagina = models.AutoField(primary_key=True, verbose_name="Id")
    pagina = models.CharField(max_length=500, verbose_name="Titulo")
    foto = models.ImageField(upload_to='pagina', verbose_name="Foto")
    descripcion = models.TextField(verbose_name="Descripcion")
    class Meta:
        db_table = 'pagina'
        ordering = ['-idpagina']
    def __unicode__(self):
        return self.pagina


class tema(models.Model):
    idtema = models.AutoField(primary_key=True, verbose_name="Id")
    tema = models.CharField(max_length=500, verbose_name="Titulo")
    class Meta:
        db_table = 'tema'
        ordering = ['-idtema']
    def __unicode__(self):
        return self.tema



class tipo_autor(models.Model):
    idtipo_autor = models.AutoField(primary_key=True, verbose_name="Id")
    tipo_autor = models.CharField(max_length=500, verbose_name="Tipo Autor")
    class Meta:
        db_table = 'tipo_autor'
        ordering = ['-idtipo_autor']
    def __unicode__(self):
        return self.tipo_autor


class autor(models.Model):
    idautor = models.AutoField(primary_key=True, verbose_name="Id")
    autor = models.CharField(max_length=500, verbose_name="Autor")
    email = models.EmailField(max_length=150, verbose_name="E-mail")
    foto = models.ImageField(upload_to='autor', verbose_name="Foto")
    tipo_autor = models.ForeignKey(tipo_autor, db_column="idtipo_autor", verbose_name="TipoAutor")
    class Meta:
        db_table = 'autor'
        ordering = ['idautor']
    def __unicode__(self):
        return self.autor


class blog(models.Model):
    idblog = models.AutoField(primary_key=True, verbose_name="Id")
    blog = models.CharField(max_length=500, verbose_name="Titulo")
    autor = models.ForeignKey(autor, db_column="idautor", verbose_name="Autor")
    tipo_autor = models.ForeignKey(tipo_autor, db_column="idtipo_autor", verbose_name="Tipo Autor")
    fecha = models.DateField(verbose_name="Fecha")
    resumen = models.TextField(verbose_name="Resumen")
    texto = models.TextField(verbose_name="Descripcion")
    imagen = models.ImageField(upload_to='blog', verbose_name="Imagen 1")
    tema = models.ForeignKey(tema, db_column="idtema", verbose_name="Tema")
    portada = models.BooleanField(verbose_name="Portada?")
    class Meta:
        db_table = 'blog'
        ordering = ['autor']
    def __unicode__(self):
        return self.blog


class comentario(models.Model):
    idcomentario = models.AutoField(primary_key=True, verbose_name="Id")
    blog = models.ForeignKey(blog, db_column="idblog", verbose_name="Blog")
    nombre = models.CharField(max_length=80, verbose_name="Nombre")
    comentario = models.TextField(verbose_name="Comentario")
    email = models.EmailField(max_length=80, verbose_name="Email")
    publicado = models.BooleanField(verbose_name="Publicado")
    fecha = models.DateField(auto_now_add=True, verbose_name="Fecha")
    ip = models.IPAddressField(verbose_name="IP")
    class Meta:
        db_table = 'comentario'
        ordering = ['-idcomentario']
    def __unicode__(self):
        return self.comentario


class doc(models.Model):
    iddoc = models.AutoField(primary_key=True, verbose_name="Id")
    doc = models.CharField(max_length=500, verbose_name="Titulo")
    portada = models.ImageField(upload_to='doc', verbose_name="Imagen")
    descripcion = models.TextField(verbose_name="Descripcion")
    archivo = models.FileField(upload_to='doc', verbose_name="Archivo")
    class Meta:
        db_table = 'doc'
        ordering = ['-iddoc']
    def __unicode__(self):
        return self.doc


class noticia(models.Model):
    idnoticia = models.AutoField(primary_key=True, verbose_name="Id")
    noticia = models.CharField(max_length=500, verbose_name="Titulo")
    fecha = models.DateField(verbose_name="Fecha")
    texto = models.TextField(verbose_name="Texto")
    foto = models.ImageField(upload_to='noticia', verbose_name="Foto")
    class Meta:
        db_table = 'noticia'
        ordering = ['-fecha']
    def __unicode__(self):
        return self.noticia


class enlace(models.Model):
    idenlace = models.AutoField(primary_key=True, verbose_name="Id")
    enlace = models.CharField(max_length=500, verbose_name="Título")
    url = models.URLField(max_length=600, verbose_name="Dirección web")
    texto = models.TextField(verbose_name="Texto")
    imagen = models.ImageField(upload_to='enlace', verbose_name="Imagen")
    class Meta:
        db_table = 'enlace'
        ordering = ['-idenlace']
    def __unicode__(self):
        return self.enlace


class galeria(models.Model):
    idgaleria = models.AutoField(primary_key=True, verbose_name="Id")
    galeria = models.CharField(max_length=500, verbose_name="Titulo")
    fecha = models.DateField(verbose_name="Fecha")
    class Meta:
        db_table = 'galeria'
        ordering = ['-idgaleria']
    def __unicode__(self):
        return self.galeria


class foto(models.Model):
    idfoto = models.AutoField(primary_key=True, verbose_name="Id")
    galeria = models.ForeignKey(galeria, db_column="idgaleria", verbose_name="Galeria")
    foto = models.CharField(max_length=500, verbose_name="Titulo")
    imagen = models.ImageField(upload_to='foto', verbose_name="Foto")
    class Meta:
        db_table = 'foto'
        ordering = ['-galeria', '-idfoto']
    def __unicode__(self):
        return self.foto


class agenda(models.Model):
    idagenda = models.AutoField(primary_key=True, verbose_name="Id")
    agenda = models.CharField(max_length=500, verbose_name="Titulo")
    fecha = models.DateField(verbose_name="Fecha")
    lugar = models.CharField(max_length=120, verbose_name="Lugar")
    texto = models.TextField(verbose_name="Evento")
    organiza = models.CharField(max_length=500, verbose_name="Organizado por")
    class Meta:
        db_table = 'agenda'
        ordering = ['-fecha']
    def __unicode__(self):
        return self.agenda
