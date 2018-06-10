from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import transaction,IntegrityError
from django.db.models import Q
import os

@login_required
def home(request):
    return render(request,'empresa/empresa.html',{})
