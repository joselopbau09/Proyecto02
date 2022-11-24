from sys import argv
from classes.AnalisisFigura import *
from classes.DetectorVertices import *
from classes.GestorImagen import *
import numpy as np
import matplotlib.pyplot as plt

class main:

    script, imagen = argv
    nombreImagen = "assets/%s"%imagen
    gi = GestorImagen(nombreImagen)
    gi.separadorFiguras()

    figuras = gi.obtenerAlmacenador()
    total = len(figuras) - 1
    i = 0

    while (i <= total):

        imagen = figuras.pop(0)
        newNumpy1 = np.array(imagen)
        af = AnalisisFigura(newNumpy1.tolist())
        centro_x, centro_y = af.buscadorCentro()
        hipotenusa = af.calculaHipotenusa()
        arregloRayos = af.rayos(centro_x, centro_y, hipotenusa)
        

        di = DetectorVertices(arregloRayos)
        vertices2 = di.suavizaDistancias()
        vertices = di.detectaVertices()
        
        plt.plot(arregloRayos)
        plt.plot(vertices2)
        plt.show()

        print(di.clasificaFigura(vertices))
        i += 1