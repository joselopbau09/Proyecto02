class AnalisisFigura:

    def buscadorCentro(self, imagenFigura):
        suma_x = 0
        suma_y = 0
        numPixeles = 0
        min_x = len(self.imagenFigura)
        max_x = 0
        min_y = len(self.imagenFigura)
        max_y = 0
        colorFondo = self.imagenFigura[0][0]
        for i in range(1,len(self.imagenFigura)):
            for j in range(1,len(self.imagenFigura)):
                colorPixel = self.imagenFigura[i][j]
                if(colorPixel != colorFondo):
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
        return centro_x, centro_y, h