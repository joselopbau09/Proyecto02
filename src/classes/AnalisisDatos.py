class AnalisisDatos:

    def __init__(self, arregloRayos):
        self.arregloRayos = arregloRayos

    def cambiarArreglo(self, nuevoArreglo):
        self.arregloRayos = nuevoArreglo

    def analizaArreglo(self):
        sumas = []
        longArreglo = len(self.arregloRayos)
        for i in range(longArreglo):
            suma = 0
            for j in range(5):
                if((i+j+1) < longArreglo):
                    suma += self.arregloRayos[i+j+1] - self.arregloRayos[i+j]
                else:
                    suma += self.arregloRayos[i+j+1 - longArreglo] - self.arregloRayos[i+j - longArreglo]
            sumas.append(suma)
        maximos = self.encuentraMaximos(sumas)
        return maximos

    def encuentraMaximos(self, sumas):
        maximos = 0
        for i in range(len(sumas)):
            if((i+1) < len(sumas)):
                if((sumas[i] >= 0 and sumas[i+1] < 0) or (sumas[i] > 0 and sumas[i+1] <= 0)):
                    maximos += 1
        return maximos