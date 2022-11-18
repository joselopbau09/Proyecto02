class DeetectorVertices:
    
    def __init__(self, distancias):
        self.distancias = distancias


    def suavizaDistancias(self):
        dist_suavizadas = []
        for i in range(len(self.distancias)):
            if(i < 2):
                dist_suavizadas.append(self.promedioDistancias(self.distancias[i:i+2]))
            elif(i > len(dist_suavizadas)-2):
                dist_suavizadas.append(self.promedioDistancias(self.distancias[i-2:i]))
            else:
                dist_suavizadas.append(self.promedioDistancias(self.distancias[i-2:i+2]))

        self.distancias = dist_suavizadas
        #print("Dist_suavizadas: " + str(dist_suavizadas))
    

    def vertices(self):
        valor_vertice = 0
        indice_vertice = 0
        promedio_dist = self.promedioDistancias(self.distancias)
        indices_vertices = []
        
        for i, valor in enumerate(self.distancias):
            if valor > promedio_dist:
                if valor_vertice == 0 or valor > valor_vertice:
                    valor_vertice = valor
                    indice_vertice = i

            elif valor < promedio_dist and indice_vertice != 0:
                    indices_vertices.append(indice_vertice)
                    indice_vertice = 0
                    valor_vertice = 0

        if indice_vertice != 0:
            indices_vertices.append(indice_vertice)
        #print("Indices: " + str(indices_vertices))
        return indices_vertices

        
    def promedioDistancias(self, distancias):
        suma = 0
        for val in distancias:
            suma = suma + val
        promedio = suma / len(distancias)
        return promedio


    def detectaVertices(self):
        self.suavizaDistancias()
        vertices = self.vertices()
        print('La prueba tiene ' + str(len(vertices)) + ' vértices')
    
def main():

    distancia_prueba1 = [3.0, 3.1, 3.3, 3.4, 3.6, 4.0, 4.2, 4.5, 4.7, 4.6, 4.3, 4.0, 3.8, 3.6, 3.5, 3.6, 3.7, 3.9, 4.0, 4.3, 4.6, 4.8, 4.5, 4.2, 4.0, 3.6, 3.4, 3.3, 3.1, 3.0, 3.1, 3.3, 3.4, 3.6, 4.0, 4.2, 4.5, 4.7, 4.6, 4.3, 4.0, 3.8, 3.6, 3.5, 3.6, 3.7, 3.9, 4.0, 4.3, 4.6, 4.8, 4.5, 4.2, 4.0, 3.6, 3.4, 3.3, 3.1]
    distancia_prueba2 = [1,3,4,5,6,8,9,8,9,10,13,10,9,8,7,8,6,5,6,7,8,9,10,11,12,10,9,8,7,5,4,3,1]
    distancia_prueba3 = [1,2,3,4,3,2,2,3,4,5,6,7,6,5,4,3,3]

    prueba1 = DeetectorVertices(distancia_prueba1)
    prueba1.detectaVertices()

    prueba2 = DeetectorVertices(distancia_prueba2)
    prueba2.detectaVertices()

    prueba3 = DeetectorVertices(distancia_prueba3)
    prueba3.detectaVertices()

main()