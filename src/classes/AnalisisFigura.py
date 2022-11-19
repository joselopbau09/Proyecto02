import math

class AnalisisFigura:

    def __init__(self, imagenFigura):
        self.imagenFigura = imagenFigura
        self.colorFondo = self.imagenFigura[0][0]

    def cambiarImagen(self,imagenFigura):
        self.imagenFigura = imagenFigura
        self.colorFondo = self.imagenFigura[0][0]

    def buscadorCentro(self):
        suma_x = 0
        suma_y = 0
        numPixeles = 0
        min_x = len(self.imagenFigura[0])
        max_x = 0
        min_y = len(self.imagenFigura)
        max_y = 0
        for j in range(1,len(self.imagenFigura)):
            for i in range(1,len(self.imagenFigura[0])):
                colorPixel = self.imagenFigura[j][i]
                if(colorPixel != self.colorFondo):
                    suma_x += i
                    suma_y += j
                    numPixeles += 1
                    if(i < min_x):
                        min_x = i
                    if(i > max_x):
                        max_x = i
                    if(j < min_y):
                        min_y = j
                    if(j > max_y):
                        min_y = j
        centro_x = suma_x / numPixeles
        centro_y = suma_y / numPixeles
        anchura = max_x - min_x
        altura = max_y - min_y
        h = max(anchura, altura) / 2
        self.setPixel(centro_x, centro_y, [0,0,0])
        return centro_x, centro_y, h

    def calculaHipotenusa(self):
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
                        min_y = j
        anchura = max_x - min_x
        altura = max_y - min_y
        hipotenusa = max(anchura, altura) / 2
        return hipotenusa

    def setPixel(self, x, y, color):
        self.imagenFigura[int(y)][int(x)] = color

    def dentro(self, coord_x, coord_y):
        colorPixel = self.imagenFigura[int(coord_y)][int(coord_x)]
        altura = len(self.imagenFigura)
        anchura = len(self.imagenFigura[0])
        if(coord_x > anchura or coord_y > altura):
            return False
        if(colorPixel != self.colorFondo):
            self.setPixel(coord_x, coord_y, [0,0,0])
            return True
        else:
            return False

    def rayos(self, centro_x, centro_y, hipotenusa):
        arregloRayos = []
        coord_x = centro_x
        coord_y = centro_y
        for i in range(360):
            coord_x = centro_x
            coord_y = centro_y
            dx = hipotenusa * math.cos(math.radians(i))
            dy = hipotenusa * math.sin(math.radians(i))
            paso = max(abs(dx),abs(dy))
            while(self.dentro(coord_x, coord_y) == True):
                coord_x += dx / paso
                coord_y += dy / paso
            longRayo = math.sqrt((coord_x - centro_x)**2 + (coord_y - centro_y)**2)
            arregloRayos.append(longRayo)
        return arregloRayos

    def obtenerImagen(self):
        return self.imagenFigura
