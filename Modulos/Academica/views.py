from django.conf import settings
from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.

def formularioContacto(request):
    return render(request, "formularioContacto.html")

def contactar(request):
    if request.method == "POST":
        asunto = request.POST["textAsunto"]
        mensaje = request.POST["textMensaje"] + " / Email: " + request.POST["textEmail"]
        email_desde = settings.EMAIL_HOST_USER
        email_para = ["juan.rodriguez@jcode.com.co"]
        send_mail(asunto,mensaje,email_desde,email_para, fail_silently=False)
        return render(request, "contactoExitoso.html")
    return render(request, "formularioIncorrecto.html")