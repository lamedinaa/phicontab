from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction,IntegrityError
from django.db.models import Q
import os

@login_required
def inicio(request):
    print "inicio hola mundo"
    return render(request,'empresa/inicio.html',{
    "active":{1:"inicio"},
    "subtitulo": "Inicio" ,
     })

@login_required
def puc(request):
    return render(request,'empresa/puc.html',{
    "active":{1:"puc"},
    "subtitulo": "Puc",
     })

@login_required
def reportes(request):
    print "reportes"
    return render(request,'empresa/reportes.html',{
    "active":{1:"reportes"},
    "subtitulo": "Reportes",
     })

@login_required
def libro(request):
    print "libros"
    return render(request,'empresa/libro.html',{
    "active":{1:"libro"},
    "subtitulo": "Libros" ,
     })

@login_required
def inventarios(request):
    print "inventarios"
    return render(request,'empresa/inventarios.html',{
    "active":{1:"inventarios"},
    "subtitulo": "Inventarios" ,
     })
