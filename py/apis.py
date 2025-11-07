# py/apis.py
from flask import Blueprint, request, jsonify,redirect
from py.db import db
import base64

apis = Blueprint("apis", __name__)

class Info(db.Model):
    __tablename__ = "info"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(50))
    tamano = db.Column(db.BigInteger)
    pixel = db.Column(db.LargeBinary)
    sobre_mi = db.Column(db.String(400), nullable=False)
    tel = db.Column(db.String(400), nullable=False)
    mail = db.Column(db.String(400), nullable=False)
    dir = db.Column(db.String(400), nullable=False)
    edad = db.Column(db.Integer, nullable=False)

class Experiencia(db.Model):
    __tablename__ = "Experiencia"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    exp = db.Column(db.String(400), nullable=False)

class Proyectos(db.Model):
    __tablename__ = "Proyectos"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pro = db.Column(db.String(400), nullable=False)

class Educacion(db.Model):
    __tablename__ = "EDUCACIÓN"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    edu = db.Column(db.String(400), nullable=False)

class Links(db.Model):
    __tablename__ = "links"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(400), nullable=False)
    url = db.Column(db.String(400), nullable=False)

class carrusel(db.Model):
    __tablename__ = "carrusel"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    tipo = db.Column(db.String(50))
    tamano = db.Column(db.BigInteger)
    pixel = db.Column(db.LargeBinary)

def validate_fields(data, required):
    missing = [f for f in required if f not in data or data[f] is None]
    return missing

@apis.route("/Info/agregar", methods=["POST","Get"])
def add_Info():
    data = request.form

    archivo = request.files.get("archivo")

    tipo = ""
    tamano = 0
    pixel = None

    tipo = archivo.content_type
    pixel = archivo.read()
    tamano = len(pixel)

    nuevo = Info(
        tipo = tipo,
        tamano = tamano,
        pixel = pixel,
        sobre_mi = data.get("sobre_mi"),
        tel = data.get("tel"),
        mail = data.get("mail"),
        dir = data.get("dir"),
        edad = 0 
    )

    try:
        db.session.add(nuevo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Error al guardar: {e}", 500

    return redirect("/")

@apis.route("/Info/editar", methods=["POST","Get"])
def update_info():
    data = request.form
    info=Info.query.first()
    archivo = request.files.get("archivo")
    
    tipo = ""
    tamano = 0
    pixel = None
    if archivo:
        tipo = archivo.content_type
        pixel = archivo.read()
        tamano = len(pixel)
        info.tipo = tipo
        info.tamano = tamano
        info.pixel = pixel
        
    info.sobre_mi = data.get("sobre_mi")
    info.tel = data.get("tel")
    info.mail = data.get("mail")
    info.dir = data.get("dir")


    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Error al guardar: {e}", 500

    return redirect("/")




@apis.route("/url", methods=["POST"])
def add_url():
    if request.method == 'POST':
        new_name = request.form['nombre']
        new_url = request.form['url']
        new_example = Links(name=new_name,url=new_url)
        db.session.add(new_example)
        db.session.commit()
        return redirect("/")

@apis.route("/url/delete/<int:id>")
def delete_url(id):
    link = Links.query.get_or_404(id)
    db.session.delete(link)
    db.session.commit()
    return redirect("/")

@apis.route("/carrusel/agregar", methods=["POST","Get"])
def add_carrusel():
    archivo = request.files.get("archivo")

    tipo = ""
    tamano = 0
    pixel = None

    tipo = archivo.content_type
    pixel = archivo.read()
    tamano = len(pixel)

    nuevo = carrusel(
        tipo = tipo,
        tamano = tamano,
        pixel = pixel
    )

    try:
        db.session.add(nuevo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Error al guardar: {e}", 500

    return redirect("/")

@apis.route("/carrusel/delete/<int:id>")
def carrusel_url(id):
    cell = carrusel.query.get_or_404(id)
    db.session.delete(cell)
    db.session.commit()
    return redirect("/")

