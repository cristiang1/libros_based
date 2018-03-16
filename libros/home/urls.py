from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
   	path('autor/', Vista_autor, name="autor"),
   	path('libro/', Vista_libro, name="libros"),
   	path('index/', Vista_index, name="inicio"),
 

]