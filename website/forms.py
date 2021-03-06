from django import forms
from django.forms import ModelChoiceField, BooleanField

from captcha.fields import CaptchaField

from models import Perfil

class CartaForm(forms.Form):
    nombre_destinatario = ModelChoiceField(queryset=Perfil.objects.all())
    colectiva = BooleanField(label="Esta carta es colectiva, sin destinatario particular.", required=False)
    asunto = forms.CharField(max_length=100)
    mensaje = forms.CharField(widget=forms.Textarea(attrs={'cols':'80', 'style':'width: 486px; height: 174px;'}))
    nombre_remitente = forms.CharField()
    archivo = forms.FileField(label="Carta escaneada (opcional)", required=False)
    correo_remitente = forms.EmailField(label="Correo del remitente (opcional)", required=False)
    cc = forms.BooleanField(label="Recibir copia del mensaje", required=False)
    captcha = CaptchaField()
