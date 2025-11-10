# py/rutas.py
from flask import render_template,Blueprint
import base64
from py.apis import Info, Educacion, Experiencia, Proyectos, Links,carrusel
from py.db import db

rutas = Blueprint('rutas', __name__, template_folder='templates')

@rutas.route("/")
def Index():
    links = Links.query.order_by(Links.id).all()
    infos = Info.query.order_by(Info.id).all()
    educaciones = Educacion.query.order_by(Educacion.id).all()
    experiencias = Experiencia.query.order_by(Experiencia.id).all()
    proyectos = Proyectos.query.order_by(Proyectos.id).all()
    Carrusel=carrusel.query.order_by(carrusel.id).all()
    
    pixeles_cell=[]
    pixel_info=""
    Indexes_cells=[]
    pixel_proyecto=[]

    for cell in Carrusel:
        Indexes_cells.append(cell.id)
        pixeles_cell.append( base64.b64encode(cell.pixel).decode("utf-8"))
    for proyecto in proyectos:
        pixel_proyecto.append( base64.b64encode(proyecto.pixel).decode("utf-8"))
    
    Len=len(infos)
    if Len!=0:
        pixel_info = base64.b64encode(infos[0].pixel).decode("utf-8")
    len_carrucel=len(pixeles_cell)
    return render_template(
        'Index.html',Links=links,Info=infos,
        Educacion=educaciones,Experiencia=experiencias,
        Proyectos=proyectos,Len=Len,pixel=pixel_info,
        carrusel=Carrusel,pixeles_cell=pixeles_cell,
        len_carrucel=len_carrucel,Indexes_cells=Indexes_cells,
        pixel_proyecto=pixel_proyecto
    )



