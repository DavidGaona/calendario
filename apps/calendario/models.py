from django.db import models


# Create your models here.


class Actividad(models.Model):
    nombre = models.CharField(max_length=255)
    # En dias
    dias_habiles = models.IntegerField(default=0)
    dias_calendario = models.IntegerField(default=0)
    descripcion = models.TextField(default="")
    maximo_deducible = models.IntegerField(default=0)
    estado = models.BooleanField(default=True)

    @staticmethod
    def obtener_actividades_activas():
        return Actividad.objects.filter(estado=True)

    @staticmethod
    def obtener_actividad(id_actividad):
        return Actividad.objects.filter(id=id_actividad)


class Calendario(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre

    @staticmethod
    def obtener_id(nombre_cal):
        return Calendario.objects.filter(nombre=nombre_cal)[0]


class ActividadCalendario(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE)
    prioridad = models.IntegerField(null=True)
    fecha_inicio_esperada = models.DateField(null=True)
    fecha_inicio_real = models.DateField(null=True)
    DIAS = (
    ('Ninguno', 'Ninguno'), ('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'),
    ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo'))
    debe_ser_dia_especifico = models.TextField(default='Ninguno', choices=DIAS)
    duracion_real = models.IntegerField(null=True)

    def __str__(self):
        return self.actividad.nombre

    @staticmethod
    def inicializar_calendario(calendario_s):
        actividades_activas = Actividad.obtener_actividades_activas()
        i = 1
        for actividad_activa in actividades_activas:
            nuevo = ActividadCalendario(
                actividad=actividad_activa,
                calendario=calendario_s,
                prioridad=i
            )
            i = i + 1
            nuevo.save()
