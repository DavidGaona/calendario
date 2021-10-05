from django.shortcuts import render, redirect

from .forms import ActividadForm, EditarActividadForm, CrearCalendarioForm, EditarCalendarioForm
from .models import Actividad, Calendario, ActividadCalendario


def actividades(request):
    actividades_activas = Actividad.objects.all()
    context = {
        'actividades': actividades_activas
    }
    return render(request, "actividad.html", context)


def calendario(request):
    actividades_activas = ActividadCalendario.objects.all()
    context = {
        'actividades': actividades_activas
    }
    return render(request, "calendario.html", context)


def crear_actividad(request):
    form = ActividadForm()

    if request.method == 'POST':
        form = ActividadForm(request.POST)
        if form.is_valid():
            form.save()
            form = ActividadForm()

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
    form = CrearCalendarioForm()

    if request.method == 'POST':
        form = CrearCalendarioForm(request.POST)
        if form.is_valid():
            form.save()
            bady = str(request.body)
            nombre = ""
            for i in range(len(bady)):
                if bady[len(bady) - 1 - i] == "=":
                    nombre = nombre[:-1]
                    break
                nombre = bady[len(bady) - 1 - i] + nombre
            id_calendario = Calendario.obtener_id(nombre)
            print(id_calendario)
            ActividadCalendario.inicializar_calendario(id_calendario)
            form = CrearCalendarioForm()

    context = {"form": form}
    return render(request, "crear-calendario.html", context)


def editar_calendario(request, pk):
    actividad = ActividadCalendario.objects.get(id=pk)
    form = EditarCalendarioForm(instance=actividad)

    if request.method == 'POST':
        form = EditarCalendarioForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('calendario')

    context = {"form": form}
    return render(request, "editar-calendario.html", context)
