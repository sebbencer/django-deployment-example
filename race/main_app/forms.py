from django import forms
from main_app.models import Runner

class NewRunnerForm(forms.ModelForm):

    class Meta():
        model = Runner
        exclude = ['number','time']
        labels = {'document_type':'Tipo de documento',
                'document_number':'Número de documento',
                'first_name':'Primer nombre',
                'second_name':'Segundo nombre',
                'first_lastname':'Primer apellido',
                'second_lastname':'Segundo apellido',
                'cellphone':'Número de celular',
                'address':'Dirección',
                'email':'Correo electrónico',
                'gender':'Sexo',
                'health':'EPS',
                'birth':'Fecha de nacimiento',
                'blood_type':'Tipo de sangre',
                'emergency_contact':'Nombre contacto de emergencia',
                'emergency_contact_cellphone':'Número de télefono contacto'}


class ConsultForm(forms.Form):
    number = forms.IntegerField()
