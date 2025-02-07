from django.contrib import admin
from django.urls import path,include #include: atribui o app existente ao url



urlpatterns = [
    path('admin/', admin.site.urls),
    #todo url que será criado na app.urls sera uncluido 'include' 
    path('', include('recipes.urls')),
    path('recipes/', include('recipes.urls')), #dominio.com/recipes/
]
