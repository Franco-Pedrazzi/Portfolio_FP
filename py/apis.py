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

def validate_fields(data, required):
    missing = [f for f in required if f not in data or data[f] is None]
    return missing

@apis.route("/api/info", methods=["POST"])
def add_info():
    data = request.get_json()
    required = ["sobre_mi", "tel", "mail", "dir", "edad"]
    missing = validate_fields(data, required)
    if missing:
        return jsonify(success=False, error=f"Faltan campos: {', '.join(missing)}"), 400
    nuevo = Info(**{k: data.get(k) for k in ["tipo", "tamano", "pixel", "sobre_mi", "tel", "mail", "dir", "edad"]})
    db.session.add(nuevo)
    db.session.commit()
    return jsonify(success=True, info={"id": nuevo.id})

@apis.route("/api/info/<int:id_info>", methods=["PUT"])
def update_info(id_info):
    info = Info.query.get(id_info)
    if not info:
        return jsonify(success=False, error="Info no encontrada"), 404
    data = request.get_json()
    for k in ["tipo", "tamano", "pixel", "sobre_mi", "tel", "mail", "dir", "edad"]:
        if k in data:
            setattr(info, k, data[k])
    db.session.commit()
    return jsonify(success=True, info={"id": info.id})

@apis.route("/api/info/<int:id_info>", methods=["DELETE"])
def delete_info(id_info):
    info = Info.query.get(id_info)
    if not info:
        return jsonify(success=False, error="Info no encontrada"), 404
    db.session.delete(info)
    db.session.commit()
    return jsonify(success=True, deleted=id_info)

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
