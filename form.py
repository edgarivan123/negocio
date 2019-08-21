from wtforms import Form
from wtforms import StringField
from wtforms import IntegerField
from wtforms.validators import DataRequired


class AgeForm(Form):
#    name = StringField('name', validators=[DataRequired()])
#    age = IntegerField('age', validators=[DataRequired()])
    nombrecompleto = StringField('nombrecompleto', validators=[DataRequired()])
    direccion = StringField('direccion', validators=[DataRequired()])
    calle = StringField('calle', validators=[DataRequired()])
    ciudad = StringField('ciudad', validators=[DataRequired()])
    estado = StringField('estado', validators=[DataRequired()])
    codigopostal = IntegerField('codigopostal', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
    tel = IntegerField('tel', validators=[DataRequired()])
    numerotarjeta = IntegerField('numerotarjeta', validators=[DataRequired()])
    nombre2 = StringField('nombre2', validators=[DataRequired()])
    fecha = IntegerField('fecha', validators=[DataRequired()])
    codigoseguridad = IntegerField('codigoseguridad', validators=[DataRequired()])

class EmailForm(Form):
       #email=StringField('email', validators=[DataRequired()])
       nombrecompleto = StringField('nombrecompleto', validators=[DataRequired()])
       direccion = StringField('direccion', validators=[DataRequired()])
       calle = StringField('calle', validators=[DataRequired()])
       ciudad = StringField('ciudad', validators=[DataRequired()])
       estado = StringField('estado', validators=[DataRequired()])
       codigopostal = IntegerField('codigopostal', validators=[DataRequired()])
       email = StringField('email', validators=[DataRequired()])
       tel = IntegerField('tel', validators=[DataRequired()])
       numerotarjeta = IntegerField('numerotarjeta', validators=[DataRequired()])
       nombre2 = StringField('nombre2', validators=[DataRequired()])
       fecha = IntegerField('fecha', validators=[DataRequired()])
       codigoseguridad = IntegerField('codigoseguridad', validators=[DataRequired()])

def legal_or_not(age):
    return (age >= 18)
