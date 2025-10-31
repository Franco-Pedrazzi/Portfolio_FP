# py/rutas.py
from flask import render_template,Blueprint
import base64
from py.apis import Info, Educacion, Experiencia, Proyectos, Links
from py.db import db

rutas = Blueprint('rutas', __name__, template_folder='templates')

@rutas.route("/")
def Index():
    links = Links.query.order_by(Links.id).all()
    infos = Info.query.order_by(Info.id).all()
    educaciones = Educacion.query.order_by(Educacion.id).all()
    experiencias = Experiencia.query.order_by(Experiencia.id).all()
    proyectos = Proyectos.query.order_by(Proyectos.id).all()

    for info in infos:
        if info.pixel:
            info.pixel = base64.b64encode(info.pixel).decode("utf-8")

    return render_template(
        'Index.html',
        Links=links,
        Info=infos,
        Educacion=educaciones,
        Experiencia=experiencias,
        Proyectos=proyectos
    )



