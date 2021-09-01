from .models import Usuario
from django import forms

import datetime


# class UsuarioForm(forms.ModelForm):

#     ## change the widget of the date field.
#     dob = forms.DateField(
#         label='tu nombre', 
#         widget=forms.CharField(max_length=100)

#     )

    

#     def __init__(self, *args, **kwargs):
#         super(UsuarioForm, self).__init__(*args, **kwargs)
#         ## add a "form-control" class to each form input
#         ## for enabling bootstrap
#         for name in self.fields.keys():
#             self.fields[name].widget.attrs.update({
#                 'class': 'form-control',

#             })


#     class Meta:

#         model = Friend

#         fields = ("__all__")

"""class Responder_Form(forms.Form):

	class Meta:
		fields = ["texto"]

		widgets = {

			'texto':forms.TextInput(

				attrs = {'id':'n_pregunta', 'placeholder':'Escribe tu respuesta'}

				)

		}"""

"""class UsuarioForm(forms.ModelForm):

	class Meta:
		fields = ["texto"]

		widgets = {

			'texto':forms.TextInput(

				attrs = {'id':'n_pregunta', 'placeholder':'Escribe tu nickname'}

				)

		}"""