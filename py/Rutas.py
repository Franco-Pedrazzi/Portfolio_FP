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
    
    pixeles_cell=[]
    pixel_info=""
    Indexes_cells=[]
    pixel_proyecto=[]

    for proyecto in proyectos:
        pixel_proyecto.append( base64.b64encode(proyecto.pixel).decode("utf-8"))
    
    len_carrucel=len(proyectos)
    Len=len(infos)
    if Len!=0:
        pixel_info = base64.b64encode(infos[0].pixel).decode("utf-8")
    
    return render_template(
        'Index.html',Links=links,Info=infos,
        Educaciones=educaciones,Experiencias=experiencias,
        Proyectos=proyectos,Len=Len,pixel=pixel_info
        ,pixeles_cell=pixeles_cell,len_carrucel=len_carrucel,
        Indexes_cells=Indexes_cells,pixel_proyecto=pixel_proyecto
    )



