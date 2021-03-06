#-*- coding: utf-8 -*-
from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField, DateField, SubmitField, PasswordField, IntegerField
from wtforms_html5 import IntegerField
from models import db, Cuidados,  Veterinario, Tratamiento



class CuidadosForm(Form):
  nombrecuidador = TextField("Cuidador")
  nombrecomidadura = TextField("Que comida dura?")
  nombrecomidablanda = TextField("Que comida blanda?")
  pautasalimentacion = TextAreaField("Como darle de comer?")
  tipohigiene = TextField("Que hay que limpiar?")
  pautashigiene = TextAreaField("Como limpiar?")
  submit = SubmitField("Guarda mis datos")
 
  def __init__(self, *args, **kwargs):
    Form.__init__(self, *args, **kwargs)
 
  def validate(self):
    if not Form.validate(self):
      return False

class VeterinarioForm(Form):
   nombreveterinario = TextField("Nombre Veterinario")
   tlfnoveterinario = TextField("Num Tlfno")
   tlfnourgencias = TextField("Num Urgencias")
   direccionveterinario = TextAreaField("Direccion")
   emailveterinario = TextField("Email")
   submit = SubmitField("Guarda los datos")

   def __init__(self, *args, **kwargs):
     Form.__init__(self, *args, **kwargs)

   def validate(self):
     if not Form.validate(self):
       return False


