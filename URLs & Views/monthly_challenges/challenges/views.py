from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def monthly_challenge(request, month):
    return HttpResponse(f"{month}")