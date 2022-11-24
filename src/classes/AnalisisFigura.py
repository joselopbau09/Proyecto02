import math

""" Módulo AnalisisFigura """
class AnalisisFigura:
    """ Clase que se encarga del análisis de cada figura dentro de la imagen.

    Atributos: 
        imagenFigura (arreglo2D): Arreglo que contiene la información de cada
            pixel de la imagen que únicamente contiene una figura con el fondo.
        colorFondo (tupla): Tupla RGB con el color de fondo
    Métodos:
        cambiarImagen(imagenFigura (arreglo2D)):
            Cambia los atributos de la clase por los de una nueva imagen.
        buscadorCentro():
            Busca las coordenadas del centro de la figura en la imagen.
        calcularHipotenusa():
            Calcula un radio alrededor de la figura.
        dentro(coord_x(int),coord_y(int)):
            Verifica si la coordenada especificada está dentro de la figura.
        rayos(centro_x(int),centro_y(int),hipotenusa(float)):
            Crea un arreglo de longitudes de rayos del centro de la figura.
        obtenerImagen():
            Getter para la imagen.
    """

    def __init__(self, imagenFigura):
        """ 
        Constructor que inicializa los atributos de la clase.
        """
        self.imagenFigura = imagenFigura
        self.colorFondo = self.imagenFigura[0][0]

    def cambiarImagen(self,imagenFigura):
        """
        Cambia los atributos de la clase por los de una nueva imagen.

        Parámetros:
            imagenFigura (arreglo2D): Arreglo de la nueva imagen a analizar.
        """
        self.imagenFigura = imagenFigura
        self.colorFondo = self.imagenFigura[0][0]

    def buscadorCentro(self):
        """
        Busca las coordenadas en x e y del centro de la figura en la imagen.
        Recorre la imagen vertical y horizontalmente sumando las posiciones
        en x e y si el pixel pertenece a la figura, además de aumentar el
        conteo del total de pixeles de la figura. Al final saca las coordenadas
        del centro promediando ambas sumas.

        Regresa:
            Coordenada x y coordenada y en la imagen del centro de la figura. (int,int)
        """
        suma_x = 0
        suma_y = 0
        numPixeles = 0
        for j in range(1,len(self.imagenFigura)):
            for i in range(1,len(self.imagenFigura[0])):
                colorPixel = self.imagenFigura[j][i]
                if(colorPixel != self.colorFondo):
                    suma_x += i
                    suma_y += j
                    numPixeles += 1
        centro_x = suma_x / numPixeles
        centro_y = suma_y / numPixeles
        return centro_x, centro_y

    def calculaHipotenusa(self):
        """
        Calcula un radio alrededor de la figura con el fin de aproximar
        su borde para poder usarlo como hipotenusa en el método
        trigonométrico de los rayos.

        Regresa:
            hipotenusa (int): Distancia aproximada que va del centro de la
            figura al borde más lejano de la misma.
        """
        min_x = len(self.imagenFigura[0])
        max_x = 0
        min_y = len(self.imagenFigura)
        max_y = 0
        for j in range(1,len(self.imagenFigura)):
            for i in range(1,len(self.imagenFigura[0])):
                colorPixel = self.imagenFigura[j][i]
                if(colorPixel != self.colorFondo):
                    if(i < min_x):
                        min_x = i
                    if(i > max_x):
                        max_x = i
                    if(j < min_y):
                        min_y = j
                    if(j > max_y):
                        max_y = j
        anchura = max_x - min_x
        altura = max_y - min_y
        hipotenusa = max(anchura, altura) / 2
        return hipotenusa

    def dentro(self, coord_x, coord_y):
        """
        Determina si el pixel en la coordenada ingresada está dentro
        de la imagen y pertenece a la figura.

        Parámetros:
            coord_x (int): Coordenada en x del pixel.
            coord_y (int): Coordenada en y del pixel.

        Regresa:
            Valor de verdad que es verdadero si el pixel está dentro
            de la figura.
        """
        colorPixel = self.imagenFigura[int(coord_y)][int(coord_x)]
        altura = len(self.imagenFigura)
        anchura = len(self.imagenFigura[0])
        if(coord_x > anchura or coord_y > altura):
            return False
        if(colorPixel != self.colorFondo):
            return True
        else:
            return False

    def rayos(self, centro_x, centro_y, hipotenusa):
        """
        Método que crea un arreglo de distancias entre el centro de la
        figura y el borde que se encuentra siguiendo un rayo aproximadamente
        en línea recta con ángulos que van desde 0 hasta 360 grados.

        Parámetros:
            centro_x (int): Coordenada en x del centro.
            centro_y (int): Coordenada en y del centro.
            hipotenusa (float): Longitud de la distancia calculada del centro
            a los bordes.
        
        Regresa:
            arregloRayos (lista): Lista que contiene las distancias
            del centro al borde por cada uno de los 360 grados.
        """
        arregloRayos = []
        coord_x = centro_x
        coord_y = centro_y
        for i in range(360):
            coord_x = centro_x
            coord_y = centro_y
            dx = hipotenusa * math.cos(math.radians(i))
            dy = hipotenusa * math.sin(math.radians(i))
            paso = max(abs(dx),abs(dy))
            while(self.dentro(coord_x, coord_y)):
                coord_x += dx / paso
                coord_y += dy / paso
            longRayo = math.sqrt((coord_x - centro_x)**2 + (coord_y - centro_y)**2)
            arregloRayos.append(longRayo)
        return arregloRayos

    def obtenerImagen(self):
        """
        Método getter para obtener el estado del arreglo
        que representa la imagen.

        Regresa:
            imagenFigura (arreglo2D): El arreglo con la información
            de la imagen.
        """
        return self.imagenFigura
