from PIL import Image
import copy
from numpy import asarray

""" Módulo GestorImagen """
class GestorImagen:
    """ Clase que se encarga de hacerla lectura de la imagen y crear una copia para cada figura de la imagen. 

    Attributes: 
        matrizImagen (list): Almacena el valor RGB de cada pixel de la imagen.
        almacenadorFiguras (list): Contiene las representaciones en matriz las figuras por separado.


    """

    def __init__(self, imagen):
        """ Constructor que transforma una imagen en su representación matricial, e inicializa los atributos de la clase.

        """
        img = Image.open(f'{imagen}')
        self.matrizImagen = asarray(img).tolist()
        self.almacenadorFiguras = []

    def buscadorColoresImagen(self):
        """ Método que se encarga obtener los colores que se encuentran en la imagen.

        Returns:
            list: Colores en formato RGB de cada color.

        """

        coloresImagen = []
        coloresImagen.append(self.matrizImagen[0][0])
        for i in range(1,len(self.matrizImagen)):
            for j in range(1, len(self.matrizImagen[0])):
                if(self.matrizImagen[i][j] not in coloresImagen):
                    coloresImagen.append(self.matrizImagen[i][j])

        return coloresImagen            
    
    def separadorFiguras(self):
        """ Método que crea las copias para cada figura en particular y las guarda en almacenadorFiguras.

        """

        colores = self.buscadorColoresImagen()
        colorFondo = colores.pop(0)
        while( len(colores) != 0):
            imagen =copy.deepcopy( self.obtenerMatriz())
            colorFigura = colores.pop()
            for i in range(1,len(imagen)):
                for j in range(1, len(imagen[0])):
                    if(( imagen[i][j] != colorFondo) and ( imagen[i][j] != colorFigura)):
                        imagen[i][j] = colorFondo
            self.almacenadorFiguras.append(imagen)
    
    def obtenerMatriz(self):
        """ Método que se encarga de obtener el atributo matrizImagen.
        
        Returns:
            list: Representación matricial de la imagen.

        """

        return self.matrizImagen
            
    def obtenerAlmacenador(self):
        """ Método que se encarga de obtener el atributo almacenadorFiguras.
        
        Returns:
            list: Contiene las representación matricial de las imagenes de cada figura.

        """

        return self.almacenadorFiguras

