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
    tipo = db.Column(db.String(50))
    tamano = db.Column(db.BigInteger)
    pixel = db.Column(db.LargeBinary)
    descripcion = db.Column(db.String(400), nullable=False)
    titulo = db.Column(db.String(50), nullable=False)
    link = db.Column(db.String(100), nullable=False)

class Educacion(db.Model):
    __tablename__ = "EDUCACIÓN"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    edu = db.Column(db.String(400), nullable=False)

class Links(db.Model):
    __tablename__ = "links"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(400), nullable=False)
    url = db.Column(db.String(400), nullable=False)



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



@apis.route("/Proyecto/agregar", methods=["POST","Get"])
def add_Proyect():
    data = request.form



    archivo = request.files.get("archivo")

    tipo = ""
    tamano = 0
    pixel = None

    tipo = archivo.content_type
    pixel = archivo.read()
    tamano = len(pixel)

    nuevo = Proyectos(
        tipo = tipo,
        tamano = tamano,
        pixel = pixel,
        descripcion = data.get("descripcion"),
        link = data.get("link"),
        titulo = data.get("titulo")
    )

    try:
        db.session.add(nuevo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Error al guardar: {e}", 500

    return redirect("/")

@apis.route("/Proyecto/editar/<int:id>", methods=["POST","Get"])
def update_Proyect(id):
    data = request.form
    Proyecto=Proyectos.query.filter_by(id=id).first()
    archivo = request.files.get("archivo")
    
    tipo = ""
    tamano = 0
    pixel = None
    if archivo:
        tipo = archivo.content_type
        pixel = archivo.read()
        tamano = len(pixel)
        Proyecto.tipo = tipo
        Proyecto.tamano = tamano
        Proyecto.pixel = pixel
        
    Proyecto.descripcion = data.get("descripcion")
    Proyecto.link = data.get("link")
    Proyecto.titulo = data.get("titulo")


    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Error al guardar: {e}", 500

    return redirect(f"/#{data.get("titulo")}")

@apis.route("/Proyecto/delete/<int:id>")
def delete_Proyecto(id):
    Proyecto = Proyectos.query.get_or_404(id)
    db.session.delete(Proyecto)
    db.session.commit()
    return redirect("/")



@apis.route("/Experiencia/agregar", methods=["POST","Get"])
def add_Experiencia():
    data = request.form
    experiencia=data.get("Experiencia")
    nuevo = Experiencia(
        exp = experiencia
    )
    try:
        db.session.add(nuevo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()

    return redirect(f"/#{experiencia}")

@apis.route("/Experiencia/editar/<int:id>", methods=["POST","Get"])
def update_Experiencia(id):
    data = request.form
    _Experiencia=Experiencia.query.filter_by(id=id).first()
       
    _Experiencia.exp = data.get("Experiencia")

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Error al guardar: {e}", 500

    return redirect(f"/#{_Experiencia.exp }")

@apis.route("/Experiencia/delete/<int:id>")
def delete_Experiencia(id):
    _Experiencia = Experiencia.query.get_or_404(id)
    db.session.delete(_Experiencia)
    db.session.commit()
    return redirect("/#Experiencias")



@apis.route("/Educacion/agregar", methods=["POST","Get"])
def add_Educacion():
    data = request.form
    educacion=data.get("Educacion")
    nuevo = Educacion(
        edu = educacion
    )
    try:
        db.session.add(nuevo)
        db.session.commit()
    except Exception as e:
        db.session.rollback()

    return redirect(f"/#{educacion}")

@apis.route("/Educacion/editar/<int:id>", methods=["POST","Get"])
def update_Educacion(id):
    data = request.form
    _Educacion=Educacion.query.filter_by(id=id).first()
       
    _Educacion.edu = data.get("Educacion")

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        return f"Error al guardar: {e}", 500

    return redirect(f"/#{_Educacion.edu }")

@apis.route("/Educacion/delete/<int:id>")
def delete_Educacion(id):
    _Educacion= Educacion.query.get_or_404(id)
    db.session.delete(_Educacion)
    db.session.commit()
    return redirect("/#Educacion")
