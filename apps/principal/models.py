from django.db import models


empleado_choices = (
    ("PK001", "Oficina sede de la GRTSE"),
    ("PK0A0", "Zona de transmisión Villahermosa"),
    ("PK0B0", "Zona de transmisión Tuxtla"),
    ("PK0C0", "Zona de transmisión Tapachula"),
    ("PK0D0", "Zona de transmisión Istmo"),
    ("PK0E0" , "Zona de transmisión Malpaso"),
    ("PK0F0", "Zona de operación de transmisión STE"),
    ("PK0A1", "Zona de transmisión Villahermosa sector Chontalpa"),
    ("PK0B1", "Zona de transmisión Tuxtla sector Chicoasén"),
    ("PK0B2", "Zona de transmisión Tuxtla sector Angostura"),
    ("PK0D1", "Zona de transmisión Istmo sector Oaxaca potencia"),
    ("PK0E1", "Zona de transmisión Malpaso sector Peñitas"),
    
)

class Empleado(models.Model):
    RPE = models.CharField(primary_key=True, max_length=5) 
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    centro_trabajo =  models.CharField(max_length=100, choices=empleado_choices, default="PK0E0")
    foto_perfil = models.ImageField(upload_to= 'images/', blank=True, null=True) 
    def __str__ (self):
        return f"{self.nombre} {self.apellidos}"
    
    class Meta:
        db_table = 'Empleado'
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['apellidos']

class encuesta(models.Model):
    id = models.IntegerField(primary_key=True)
    pregunta = models.CharField(max_length=1000)
    categoria = models.IntegerField(null=True)
    cate = models.IntegerField(null=True)
    dominio = models.IntegerField(null=True)
    
    def __str__(self):
        return str(self.id)
    
    class Meta:
        db_table = 'encuesta'
        verbose_name = 'encuesta'
        verbose_name_plural = 'encuestas'

        ordering=['id']


class respuesta(models.Model):
    pregunta = models.ForeignKey(encuesta,on_delete=models.CASCADE)
    empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE)
    eleccion = models.IntegerField(null=True)
    
    def __str__(self):
        return str(self.empleado)
    
    class Meta:
        db_table = 'respuesta'
        verbose_name = 'respuesta'
        verbose_name_plural = 'respuestas'

class resultado(models.Model):
    empleado = models.ForeignKey(Empleado,on_delete=models.CASCADE)
    contestado = models.DateField(auto_now_add=True, auto_now= False, blank=True)
    atencion_clinica= models.BooleanField(default=False)
    total = models.IntegerField(null=True)
    cat1= models.IntegerField(null=True)
    cat2= models.IntegerField(null=True)
    cat3= models.IntegerField(null=True)
    cat4= models.IntegerField(null=True)
    cat5= models.IntegerField(null=True)
    dom1 = models.IntegerField(null=True)
    dom2 = models.IntegerField(null=True)
    dom3 = models.IntegerField(null=True)
    dom4 = models.IntegerField(null=True)
    dom5 = models.IntegerField(null=True)
    dom6 = models.IntegerField(null=True)
    dom7 = models.IntegerField(null=True)
    dom8 = models.IntegerField(null=True)
    dom9 = models.IntegerField(null=True)
    dom10 = models.IntegerField(null=True)
    comentarios = models.TextField(null=True, blank=True) 
    def __str__(self):
        return str(self.contestado)
    
    class Meta:
        db_table = 'resultado'
        verbose_name = 'resultado'
        verbose_name_plural = 'resultado'        