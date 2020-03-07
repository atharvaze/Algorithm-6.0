from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,StreamingHttpResponse
from django.views.decorators.csrf import csrf_exempt
import csv
from io import BytesIO as IO
import xlsxwriter
import pandas as pd

def base(request):
    return render(request,'login.html',{})

def home(request):
    return render(request,'home.html',{})

@csrf_exempt
def skillset(request):
	return render(request,'skillfinder.html',{})

def homepage(request):
    return render(request,'base.html',{})

def skills(request):
	skillz=request.GET.get('q')
	print(skillz)
	return render(request,'skills.html',{'skillz':skillz})
