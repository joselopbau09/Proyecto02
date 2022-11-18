import os
import numpy
from PIL import Image
from classes.GestorImagen import GestorImagen
from classes.AnalisisFigura import AnalisisFigura
from classes.AnalisisDatos import AnalisisDatos


def main():
    absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
    absolute_image_path = os.path.join(absolute_folder_path, 'assets/example_1.bmp')
    x = GestorImagen(absolute_image_path)
    #c2 = x.buscadorColoresImagen()
    x.separadorFiguras()
    
    figuras = x.obtenerAlmacenador()
    #print(len(figuras))    
    imagen1 = figuras.pop(0)
    newNumpy1 = numpy.array(imagen1)
    af = AnalisisFigura(newNumpy1.tolist())
    centro_x, centro_y, h = af.buscadorCentro()
    #print("Hipotenusa = " + str(h))
    #print("Centro en x = " + str(centro_x))
    #print("centro en y = " + str(centro_y))
    arregloRayos = af.rayos(centro_x, centro_y, h)
    #print(arregloRayos)
    """
    TODO: Parte del código que analiza el arreglo 
    ad = AnalisisDatos(arregloRayos)
    print("Lados")
    print(ad.analizaArreglo())
    """
    newNumpy2 = numpy.asarray(af.obtenerImagen())
    data1 = Image.fromarray((newNumpy2).astype(numpy.uint8))
    data1.save('example_1_03.bmp')

    #newNumpy2 = AnalisisFigura().setPixel(newNumpy1, centro_x, centro_y, [0,0,0])
    #print(newNumpy1)
    #data1 = Image.fromarray((newNumpy2).astype(numpy.uint8))
    #data1.save('example_1_02.bmp')

if __name__ == "__main__":
    main()