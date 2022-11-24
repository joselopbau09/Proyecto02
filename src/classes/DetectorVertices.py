from sys import argv

class DetectorVertices:
    """ Clase que recibe una lista con las distancias de la figura
        y la procesa para obtener el número de vértices.

        Attributes: 
        distancias (list): lista de las distancias.

    """
    
    def __init__(self, distancias):
        """Metodo que crea un objeto para dectectar los vertices
           en el arreglo con las distancias de la figura.

        """
        self.distancias = distancias


    def suavizaDistancias(self):
        """Metodo que reduce el ruido entre las distancias del centro a los extremos de la figura.
        
        """
        dist_suavizadas = []
        for i in range(len(self.distancias)):
            if(i < 15):
                dist_suavizadas.append(self.promedioDistancias(self.distancias[i:i+15]))
            elif(i > len(dist_suavizadas)-15):
                dist_suavizadas.append(self.promedioDistancias(self.distancias[i-15:i]))
            else:
                dist_suavizadas.append(self.promedioDistancias(self.distancias[i-15:i+15]))

        self.distancias = dist_suavizadas
        return dist_suavizadas
    

    def cuentaVertices(self):
        """Algoritmo para detectar los vertices de una figura usando la lista
           de distancias previamente procesada.

           Returns: 
                int: los vértices en la figura.

        """
        valor_vertice = 0
        indice_vertice = 0
        promedio_dist = self.promedioDistancias(self.distancias)
        vertices = []
        if(max(self.distancias) - min(self.distancias) < 2.5):
            pass
        else:
            for i, valor in enumerate(self.distancias):
                if valor > promedio_dist:
                    if valor_vertice == 0 or valor > valor_vertice:
                        valor_vertice = valor
                        indice_vertice = i

                elif valor < promedio_dist and indice_vertice != 0:
                        vertices.append(indice_vertice)
                        indice_vertice = 0
                        valor_vertice = 0

        if indice_vertice != 0:
            vertices.append(indice_vertice)
        return len(vertices)

        
    def promedioDistancias(self, distancias):
        """Metodo auxiliar para reducir el ruido en las distancias,
           promedia elementos en una lista.

            Args: 
                distancias (list): lista de la que se van a obtener los promedios.

            Returns:
                float: promedio de los elemnetos de la lista.
            
        """
        suma = 0
        for val in distancias:
            suma = suma + val
        promedio = suma / len(distancias)
        return promedio


    def detectaVertices(self):
        """Método para detectar vértices en el arreglo de la figura, 
            llama a otros dos métodos.

            Returns:
                int: cantidad de vértices de la figura
            
        """
        self.suavizaDistancias()
        vertices = self.cuentaVertices()
        print(vertices)
        return vertices

    
    def clasificaFigura(self, numVertices):
        """Método para clasificar figuras de acuerdo a su número de vértices.

           Args:
                numVertices (int): el número de vértices encontrado en la lista de distancias.

            Returns:
                string: el tipo de figura
        """
        if(numVertices == 0):
            return "O"
        elif(numVertices == 3):
            return "T"
        elif(numVertices == 4 or numVertices == 2):
            return "C"
        else:
            return "X"