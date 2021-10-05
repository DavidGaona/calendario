from django import forms

from .models import Actividad, Calendario, ActividadCalendario


class ActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ('nombre', 'dias_habiles', 'dias_calendario', 'maximo_deducible', 'descripcion')

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "dias_habiles": forms.NumberInput(attrs={"class": "form-control"}),
            "dias_calendario": forms.NumberInput(attrs={"class": "form-control"}),
            "maximo_deducible": forms.NumberInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control"}),
        }


class EditarActividadForm(forms.ModelForm):
    class Meta:
        model = Actividad
        fields = ('nombre', 'dias_habiles', 'dias_calendario', 'maximo_deducible', 'descripcion',
                  'estado')

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "dias_habiles": forms.NumberInput(attrs={"class": "form-control"}),
            "dias_calendario": forms.NumberInput(attrs={"class": "form-control"}),
            "maximo_deducible": forms.NumberInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control"}),
            "estado": forms.CheckboxInput()
        }


class CrearCalendarioForm(forms.ModelForm):
    class Meta:
        model = Calendario
        fields = ('nombre', )

        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"})
        }


class EditarCalendarioForm(forms.ModelForm):
    class Meta:
        model = ActividadCalendario
        fields = ('actividad', 'calendario', 'prioridad', 'fecha_inicio_esperada',
                  'debe_ser_dia_especifico')

        widgets = {
            "actividad": forms.TextInput(attrs={"class": "form-control"}),
            "calendario": forms.TextInput(attrs={"class": "form-control"}),
            "prioridad": forms.NumberInput(attrs={"class": "form-control"})
        }
