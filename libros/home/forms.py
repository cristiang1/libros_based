from django import forms

class autor_form(forms.Form):
	nombre_autor = forms.CharField(widget=forms.TextInput())

class libro_form(forms.Form):
	titulo_libro = forms.CharField(widget=forms.TextInput())