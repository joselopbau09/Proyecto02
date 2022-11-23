from sys import argv
from classes.AnalisisFigura import *
from classes.DetectorVertices import *
from classes.GestorImagen import *

class main:

    script, imagen = argv
    nombreImagen = "assets/%s"%imagen
    gi = GestorImagen(nombreImagen)
    gi.separadorFiguras()