import os
import numpy
from PIL import Image
from classes.GestorImagen import GestorImagen
from classes.AnalisisFigura import AnalisisFigura

def main():
    absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
    absolute_image_path = os.path.join(absolute_folder_path, 'assets/example_5.bmp')
    x = GestorImagen(absolute_image_path)
    #c2 = x.buscadorColoresImagen()
    x.separadorFiguras()
    figuras = x.obtenerAlmacenador()
    print(len(figuras))
    total = len(figuras) - 1  
    i = 0
    while(i <= total):
        imagen1 = figuras.pop(0)
        newNumpy1 = numpy.array(imagen1)
        af = AnalisisFigura(newNumpy1.tolist())
        centro_x, centro_y = af.buscadorCentro()
        h = af.calculaHipotenusa()
        arregloRayos = af.rayos(centro_x, centro_y, h)
        newNumpy2 = numpy.asarray(af.obtenerImagen())
        data1 = Image.fromarray((newNumpy2).astype(numpy.uint8))
        data1.save('example_5_' + str(i) + '.bmp')
        i += 1

if __name__ == "__main__":
    main()