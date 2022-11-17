from PIL import Image
import copy
import numpy
from numpy import asarray
import os

class GestorImage:

    def __init__(self, imagen):
        self.imagen = imagen
        img = Image.open(f'{imagen}')
        self.__matrizImagen = asarray(img).tolist()
        self.almacenadorFiguras = []

    def buscadorColoresImagen(self):
        coloresImagen = []
        coloresImagen.append(self.__matrizImagen[0][0])
        for i in range(1,len(self.__matrizImagen)):
            for j in range(1, len(self.__matrizImagen[0])):
                if(self.__matrizImagen[i][j] not in coloresImagen):
                    coloresImagen.append(self.__matrizImagen[i][j])

        return coloresImagen            
    
    def separadorFiguras(self):
        colores = self.buscadorColoresImagen()
        colorFondo = colores.pop(0)
        while( len(colores) != 0):
            imagen = copy.deepcopy( self.obtenerMatriz())
            colorFigura = colores.pop()
            for i in range(1,len(imagen)):
                for j in range(1, len(imagen[0])):
                    if(( imagen[i][j] != colorFondo) and ( imagen[i][j] != colorFigura)):
                        imagen[i][j] = colorFondo
            self.almacenadorFiguras.append(imagen)
    
    def obtenerMatriz(self):
        return self.__matrizImagen
            
    def obtenerImagen(self):
        return self.imagen
    
    def obtenerAlmacenador(self):
        return self.almacenadorFiguras

def main():

    absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
    absolute_image_path = os.path.join(absolute_folder_path, '../assets/example_2.bmp')
    x = GestorImage(absolute_image_path)
    #c2 = x.buscadorColoresImagen()
    x.separadorFiguras()
    
    figuras = x.obtenerAlmacenador()
    print(len(figuras))    
    imagen1 = figuras.pop(0)
    newNumpy1 = numpy.array(imagen1)
    #print(newNumpy1)
    data1 = Image.fromarray((newNumpy1).astype(numpy.uint8))
    data1.save('example_2_01.bmp')


main()