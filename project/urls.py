from django.http import HttpResponse
from django.contrib import admin
from django.urls import path

def my_view(request):
    return HttpResponse('About me')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', my_view),
]
