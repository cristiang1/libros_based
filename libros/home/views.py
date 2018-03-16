from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def Vista_index(request):
	return render(request, 'index.html')
	

def Vista_autor(request):
	info_enviado = False
	autor=""
	if request.method == "POST":
		formulario = autor_form(request.POST)
		if formulario.is_valid():
			info_enviado= True
			autor = formulario.cleaned_data['nombre_autor']
			lista = Autor.objects.filter(nombre__startswith=autor)
			list_libros = Libro.objects.all()
		return render(request,'autor.html', locals())
	else:
		formulario = autor_form()
	return render(request,'autor.html', locals())


def Vista_libro(request):
	info_enviado = False
	libro=""
	if request.method == "POST":
		formularilibro = libro_form(request.POST)
		if formularilibro.is_valid():
			info_enviado= True
			libro = formularilibro.cleaned_data['titulo_libro']
			lista = Libro.objects.filter(titulo__startswith=libro)
		return render(request,'libro.html', locals())
	else:
		formularilibro = libro_form()
	return render(request,'libro.html', locals())
