from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'global/home.html',context={
        'name' : 'Victor Souza',
    })

def contact(request):
    return HttpResponse('ZIPZAP')
def ets(request):
    return HttpResponse('Turimnha 14')
def about(request):
    return HttpResponse('Hi Guys')