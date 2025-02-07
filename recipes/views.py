from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('''<!DOCTYPE>
    <html>
       <head>
            <title>Recipes</title>    
        </head>
        <body>
            <h1>HELLO GOOD </h1>
        </body>
    </html>
    ''')

def contact(request):
    return HttpResponse('ZIPZAP')
def ets(request):
    return HttpResponse('Turimnha 14')
def about(request):
    return HttpResponse('Hi Guys')