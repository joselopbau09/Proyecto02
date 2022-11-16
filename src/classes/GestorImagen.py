from PIL import Image
import numpy
from numpy import asarray
import os

class GestorImage:

    def __init__(self, imagen):
        self.imagen = imagen
        img = Image.open(f'{imagen}')
        self.matrizImagen = asarray(img).tolist()
        self.almacenadorFiguras = []

    def buscadorColoresImagen(self):
        coloresImagen = []
        coloresImagen.append(self.matrizImagen[0][0])
        for i in range(1,len(self.matrizImagen)):
            for j in range(1, len(self.matrizImagen[0])):
                if(self.matrizImagen[i][j] not in coloresImagen):
                    coloresImagen.append(self.matrizImagen[i][j])
        return coloresImagen    

    def crearCopia(self):
        return self.matrizImagen.copy()
    
    def separadorFiguras(self):
        colores = self.buscadorColoresImagen()
        colorFondo = colores.pop(0)
        while( len(colores) != 0):
            imagen = self.crearCopia()
            colorFigura = colores.pop(0)
            for i in range(1,len(imagen)):
                for j in range(1, len(imagen[0])):
                    if(( imagen[i][j] != colorFondo) and ( imagen[i][j] != colorFigura)):
                        imagen[i][j] = colorFondo
            self.almacenadorFiguras.append(imagen)
            
    def obtenerMatriz(self):
        return self.matrizImagen
            
    def obtenerImagen(self):
        return self.imagen
    
    def obtenerAlmacenador(self):
        return self.almacenadorFiguras

def main():

    absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
    absolute_image_path = os.path.join(absolute_folder_path, '../assets/example_1.bmp')
    x = GestorImage(absolute_image_path)
    #c2 = x.buscadorColoresImagen()
    x.separadorFiguras()
    
    figuras = x.obtenerAlmacenador()    
    imagen1 = figuras.pop(0)
    newNumpy1 = numpy.array(imagen1)
    #print(newNumpy1)
    data1 = Image.fromarray((newNumpy1).astype(numpy.uint8))
    data1.save('example_1_01.bmp')


main()