from datetime import datetime, timedelta

from django.shortcuts import get_object_or_404, render
from django.shortcuts import redirect
from swingtime import models as swingtime

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


def reportes(request):
    import jwt
    import time

    METABASE_SITE_URL = "http://localhost:3000"
    METABASE_SECRET_KEY = "3e89e8f35e0e2e0082a921668ca2a20028da8628ec5252cc88f560af5277f9d5"

    payload = {
        "resource": {"dashboard": 1},
        "params": {

        },
        "exp": round(time.time()) + (60 * 10) # 10 minute expiration
    }
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

    iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token + "#theme=night&bordered=true&titled=true"
    context = {
        'reportes': iframeUrl
    }
    return render(request, "reportes.html", context)


def event_type(request, abbr):
    event_type = get_object_or_404(swingtime.EventType, abbr=abbr)
    now = datetime.now()
    occurrences = swingtime.Occurrence.objects.filter(
        event__event_type=event_type,
        start_time__gte=now,
        start_time__lte=now+timedelta(days=+30)
    )
    return render(request, 'upcoming_by_event_type.html', {
        'occurrences': occurrences,
        'event_type': event_type
    })
