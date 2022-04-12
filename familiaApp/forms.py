from django import forms


class CursoForms(forms.Form):
    nombre= forms.CharField()
    camada= forms.CharField()


class EstudianteForms(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    email=forms.EmailField()

class ProfesorForms(forms.Form):
    nombre= forms.CharField()
    apellido= forms.CharField()
    email=forms.EmailField()
    profesion=forms.CharField()
