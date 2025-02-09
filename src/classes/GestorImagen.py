
from PIL import Image
import copy
from numpy import asarray

""" Módulo GestorImagen """
class GestorImagen:
    """ Clase que se encarga de hacer la lectura de la imagen y crear una copia para cada figura de la imagen. 

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
        self.coloresImagen = []
        self.separarFiguras()

    def buscadorColoresImagen(self,):
        """ Método que se encarga obtener los colores que se encuentran en la imagen.

        Regresa:
            list: Colores en formato RGB de cada color.

        """

        coloresImagen = []
        coloresImagen.append(self.matrizImagen[0][0])
        for i in range(1,len(self.matrizImagen)):
            for j in range(1, len(self.matrizImagen[0])):
                if(self.matrizImagen[i][j] not in coloresImagen):
                    coloresImagen.append(self.matrizImagen[i][j])

        return coloresImagen            
    
    def separarFiguras(self):
        """ Método que crea las copias para cada figura en particular y las guarda en almacenadorFiguras.

        """

        colores = self.buscadorColoresImagen()
        colorFondo = colores.pop(0)
        while( len(colores) != 0):
            copiaImagen = copy.deepcopy( self.obtenerMatriz())
            colorFigura = colores.pop()
            self.coloresImagen.append(colorFigura)
            for i in range(1,len(copiaImagen)):
                for j in range(1, len(copiaImagen[0])):
                    if(( copiaImagen[i][j] != colorFondo) and ( copiaImagen[i][j] != colorFigura)):
                        copiaImagen[i][j] = colorFondo
            self.almacenadorFiguras.append(copiaImagen)
    
    def obtenerMatriz(self):
        """ Método que se encarga de obtener el atributo matrizImagen.
        
        Regresa:
            list: Representación matricial de la imagen.

        """

        return self.matrizImagen

    def obtenerColores(self):
        """ Método que se encarga de obtener el atributo coloresImagen.
        
        Regresa:
            list: Colores que se encuentran en la imagen.

        """

        return self.coloresImagen    
            
    def obtenerAlmacenador(self):
        """ Método que se encarga de obtener el atributo almacenadorFiguras.
        
        Regresa:
            list: Contiene las representación matricial de las imagenes de cada figura.

        """

        return self.almacenadorFiguras