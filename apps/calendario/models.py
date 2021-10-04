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
    nombre = models.CharField(max_length=255)
    fecha_inicio = models.DateField()


class ActividadCalendario(models.Model):
    actividad = models.ForeignKey(Actividad, on_delete=models.CASCADE)
    calendario = models.ForeignKey(Calendario, on_delete=models.CASCADE)
    prioridad = models.IntegerField(null=True)
    fecha_inicio_esperada = models.DateField()
    fecha_inicio_real = models.DateField()
    # 0 no, 1 = lunes, 2 = martes, ..., 7 = domingo
    DIAS = (('Ninguno', 'Ninguno'), ('Lunes', 'Lunes'), ('Martes', 'Martes'), ('Miércoles', 'Miércoles'),
            ('Jueves', 'Jueves'), ('Viernes', 'Viernes'), ('Sábado', 'Sábado'), ('Domingo', 'Domingo'))
    debe_ser_dia_especifico = models.TextField(default='Ninguno', choices=DIAS)
    duracion_real = models.IntegerField(null=True)

    def __str__(self):
        return self.actividad.nombre
