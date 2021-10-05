from django.shortcuts import render, redirect
from .forms import ActividadForm, EditarActividadForm, CrearCalendarioForm
from .models import Actividad
from datetime import datetime, timedelta
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404, render

from swingtime import models as swingtime


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


def reportes(request):
    import jwt
    import time

    METABASE_SITE_URL = "http://localhost:3000"
    METABASE_SECRET_KEY = "108a6d1696676b6441f305dc6478e17cbb83d2c0c688a55142a8a40ac5bb68a8"

    payload = {
        "resource": {"dashboard": 1},
        "params": {},
        "exp": round(time.time()) + (60 * 10) # 10 minute expiration
    }
    token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")
    iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token + "#theme=night&bordered=true&titled=true"
    context = {
        'reportes': iframeUrl
    }
    return render(request, "reportes.html", context)