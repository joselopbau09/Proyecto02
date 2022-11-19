from PIL import Image
import copy
from numpy import asarray

class GestorImagen:

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