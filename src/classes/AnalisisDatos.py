class AnalisisDatos:

    def __init__(self, arregloRayos):
        self.arregloRayos = arregloRayos

    def cambiarArreglo(self, nuevoArreglo):
        self.arregloRayos = nuevoArreglo

    def analizaArreglo(self):
        sumas = []
        for i in self.arregloRayos:
            for j in range(5):
                if((i+j) < len(self.arregloRayos)):
                    sumas[i] += self.arregloRayos[i+j]
        return encuentraMaximos(sumas)

    def encuentraMaximos(self, sumas):
        maximos = 0
        for i in sumas:
            if(sumas[i] >= 0 and sumas[i+1] < 0):
                maximos = maximos + 1
        return maximos
