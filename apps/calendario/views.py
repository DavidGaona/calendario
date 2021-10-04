from django.shortcuts import render, redirect
from .forms import ActividadForm, EditarActividadForm, CrearCalendarioForm
from .models import Actividad


def actividades(request):
    actividades_activas = Actividad.objects.all()
    context = {
        'actividades': actividades_activas
    }
    return render(request, "actividad.html", context)


def crear_actividad(request):
    form = ActividadForm()

    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'crear-actividad.html', context)


def editar_actividad(request, pk):
    actividad = Actividad.objects.get(id=pk)
    form = EditarActividadForm(instance=actividad)

    if request.method == 'POST':
        form = EditarActividadForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('actividades')

    context = {'form': form}
    return render(request, 'editar-actividad.html', context)


def crear_calendario(request):
    form = CrearCalendarioForm

    if request.method == 'POST':
        form = CrearCalendarioForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        "form": CrearCalendarioForm
    }
    return render(request, "actividad.html", context)

