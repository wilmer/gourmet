from django.db import models
from datetime import date,datetime

# Create your models here.
#El tipo operador puede ser cocinero o mozo
#Cocinero 1 y Mozo 0
class operador(models.Model):
    nombre_operador = models.CharField(max_length=12,null=False)
    usuario = models.CharField(max_length=12,null=False)
    password = models.CharField(max_length=12,null=False)
    tipo_operador = models.IntegerField(null=False)
    def __str__(self):
        return(self.nombre_operador+" "+self.usuario+" "+self.password)

class platodefondo(models.Model):
    descripcion_platodefondo = models.CharField(max_length=120, null=False)
    def __str__(self):
        return(self.descripcion_platodefondo)

class entrada(models.Model):
    descripcion_entrada = models.CharField(max_length=120, null=False)
    def __str__(self):
        return(self.descripcion_entrada)

class refresco(models.Model):
    descripcion_refresco = models.CharField(max_length=120, null=False)
    def __str__(self):
        return(self.descripcion_refresco)

class registroestado(models.Model):
    descripcion_registroestado = models.CharField(max_length=120, null=True)
    def __str__(self):
        return(self.descripcion_registroestado)

#actividad
class menu(models.Model):
    id_entrada_1=models.ForeignKey(entrada,on_delete=models.CASCADE,related_name="menu_entrada")
    id_entrada_2=models.ForeignKey(entrada,on_delete=models.CASCADE,related_name="menu_entrada_2")
    id_platodefondo_1 = models.ForeignKey(platodefondo,on_delete=models.CASCADE,related_name="menu_platodefondo")
    id_platodefondo_2 = models.ForeignKey(platodefondo,on_delete=models.CASCADE,related_name="menu_platodefondo_2")
    id_refresco = models.ForeignKey(refresco,on_delete=models.CASCADE,related_name="menu_refresco")
    id_operador = models.ForeignKey(operador,on_delete=models.CASCADE,related_name="menu_operador")
    descripcion_menu = models.CharField(max_length=250, null=True)
    #id_registroestado = models.ForeignKey(registroestado,on_delete=models.CASCADE,related_name="menu_registroestado")
    fecha_menu = models.DateField(blank=True, default=date.today)

class pedido(models.Model):
    id_menu=models.ForeignKey(menu,on_delete=models.CASCADE,related_name="pedido_menu")
    id_operador = models.ForeignKey(operador,on_delete=models.CASCADE, related_name="pedido_operador")
    id_registroestado = models.ForeignKey(registroestado,on_delete=models.CASCADE,related_name="pedido_registroestado")
    fecha_pedido = models.DateField(blank=True, default=date.today)
    def __str__(self):
        return(self.id_pedido+" "+self.id_operador)

class pedidoatendido(models.Model):
    id_pedido=models.ForeignKey(pedido,on_delete=models.CASCADE,related_name="pedidoatendido_pedido")
    id_operador = models.ForeignKey(operador,on_delete=models.CASCADE, related_name="pedidoatendido_operador")
    id_registroestado = models.ForeignKey(registroestado,on_delete=models.CASCADE,related_name="pedidoatendido_registroestado")
    fecha_atendido = models.DateField(blank=True, default=date.today)


class turno(models.Model):
    descripcion_turno = models.CharField(max_length=12, null=False)
    def __str__(self):
        return(self.descripcion_turno)

class equipo(models.Model):
    nombre_equipo = models.CharField(max_length=12, null=False)
    modelo = models.CharField(max_length=12, null=False)
    estado = models.IntegerField( null=False)
    def __str__(self):
        return(self.nombre_equipo+" "+self.modelo+" ")

class actividad(models.Model):
    id_turno=models.ForeignKey(turno,on_delete=models.CASCADE,related_name="actividad_turno")
    id_operador = models.ForeignKey(operador,on_delete=models.CASCADE, related_name="actividad_operador")
    id_ayudante=models.ForeignKey(operador,on_delete=models.CASCADE, related_name="actividad_ayudante",null=True)
    id_equipo=models.ForeignKey(equipo,on_delete=models.CASCADE, related_name="actividad_equipo")
    fecha_actividad = models.DateField(blank=True, default=date.today)
    nivel = models.CharField(max_length=12, null=True)


class detalle_actividad(models.Model):
    id_actividad = models.ForeignKey(actividad,on_delete=models.CASCADE, related_name="actividad_detalle_actividad")
    actividad=models.CharField(max_length=50, null=False)
    hora_inicio=models.DateTimeField(blank=True, auto_now_add=True)
    hora_fin = models.DateTimeField(blank=True, auto_now_add=True)
    codigo_operacion=models.CharField(max_length=50, null=False)
    descripcion_operacion=models.CharField(max_length=50, null=False)
    labor_origen=models.CharField(max_length=50, null=False)
    labor_destino=models.CharField(max_length=50, null=False)
    observaciones=models.CharField(max_length=50, null=False)
    tipo_material= models.CharField(max_length=50, null=False)
    labor_s=models.CharField(max_length=50, null=False)
    proyecto_s=models.CharField(max_length=50, null=False)
    fila_s=models.CharField(max_length=50, null=False)
    num_taladro_s=models.CharField(max_length=50, null=False)
    num_barras_s=models.CharField(max_length=50, null=False)
    longitud_s=models.CharField(max_length=50, null=False)
    inclinacion_s=models.CharField(max_length=50, null=False)
    num_broca_s=models.CharField(max_length=50, null=False)
    hr_diesel_inicial=models.CharField(max_length=50, null=False)
    hr_diesel_final=models.CharField(max_length=50, null=False)
    hr_electricidad_inicial_s=models.CharField(max_length=50, null=False)
    hr_electricidad_final_s=models.CharField(max_length=50, null=False)

class simba(models.Model):
    id_detalle_actividad=models.ForeignKey(detalle_actividad,on_delete=models.CASCADE,related_name="simba_detalle_actividad")
    percusion=models.CharField(max_length=20, null=False)
    longitud=models.CharField(max_length=20, null=False)
    def __str__(self):
        return(self.id_detalle_actividad+" "+self.percusion+" "+self.longitud+" "+self.longitud)


class scoop(models.Model):
    id_detalle_actividad=models.ForeignKey(detalle_actividad,on_delete=models.CASCADE,related_name="scoop_detalle_actividad")
    horometro=models.CharField(max_length=20, null=False)
    numero_cucharas=models.CharField(max_length=20, null=False)
    material=models.CharField(max_length=20, null=False)
    toneladas=models.CharField(max_length=20, null=False)
    def __str__(self):
        return(self.id_detalle_actividad+" "+self.horometro+" "+self.numero_cucharas+" "+self.material+" "+self.toneladas)
