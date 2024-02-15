from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def helloworld(request):
    return HttpResponse('Te amaulaaaaaa Maulisario <3')
