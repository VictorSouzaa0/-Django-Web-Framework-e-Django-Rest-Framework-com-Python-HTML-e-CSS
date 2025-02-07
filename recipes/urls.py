from django.urls import path
#importando todos arquivo dos views
from . import views
#criando url
# domain/recipes/about
urlpatterns = [
    path('', views.home), #home
    path('about/', views.about), #/sobre/
    path('contact/', views.contact) # /contact/
]
