from django.db import models
import datetime


DOCUMENT_CHOICES = (
    ('C.C.', 'CÉDULA DE CIUDADANÍA'),
    ('C.E.', 'CÉDULA DE EXTRANJERIA'),
    ('C.I.P.', 'CÉDULA DE IDENTIDAD POLICIAL'),
    ('C.M.', 'CÉDULA MILITAR'),
    ('C.E.I.L.', 'CÓD. ESTUDIANTE I.LENGUAS'),
    ('C.EST.', 'CÓDIGO ESTUDIANTE'),
    ('C.REG.', 'CONTRASEÑA REGISTRADURIA'),
    ('E.EXT.', 'ENTIDADES EXTRANJERAS'),
    ('L.M.', 'LIBRETA MILITAR'),
    ('NIT', 'NIT'),
    ('OTHERS', 'OTROS DOCUMENTOS'),
    ('PASSPORT', 'PASAPORTE'),
    ('C.PASSPORT', 'PASAPORTE COLOMBIANO'),
    ('R.C.', 'REGISTRO CIVIL'),
    ('R.C.', 'SIN DOCUMENTO'),
    ('T.I.', 'TARJETA DE IDENTIDAD'),
    ('TAX ID', 'TAX ID/NÚMERO DE IMPUESTO PARA'),
    ('VAT', 'VAT/NÚMERO DE IMPUESTO PARA PR'),
)

GENDER_CHOICES = (
    ('ML','MASCULINO'),
    ('FM','FEMENINO'),
    ('OTHER','OTRO'),
)

B_TYPE_CHOICES = (
    ('O-','O -'),
    ('O+','O +'),
    ('A-','A -'),
    ('A+','A +'),
    ('B-','B -'),
    ('B+','B +'),
    ('AB-','AB -'),
    ('AB+','AB +'),


)
# Create your models here.
class Runner(models.Model):
    document_type = models.CharField(max_length=128,choices=DOCUMENT_CHOICES,default='CC')
    document_number = models.CharField(max_length=128)
    first_name = models.CharField(max_length=128)
    second_name = models.CharField(max_length=128,blank=True)
    first_lastname = models.CharField(max_length=128)
    second_lastname = models.CharField(max_length=128)
    cellphone = models.CharField(max_length=128,unique=True)
    address = models.CharField(max_length=128)
    email = models.EmailField(max_length=264,unique=True)
    gender = models.CharField(max_length=128,choices=GENDER_CHOICES,default='ML')
    health = models.CharField(max_length=128)
    birth = models.DateField(default=datetime.date.today)
    blood_type = models.CharField(max_length=128,choices=B_TYPE_CHOICES,default='O-')
    emergency_contact = models.CharField(max_length=128)
    emergency_contact_cellphone = models.CharField(max_length=128)
    number = models.PositiveIntegerField(default=0)
    time = models.TimeField(null=True)
    class Meta:
        unique_together = ('document_type','document_number')

#class StudentUISRunner(Runner):
