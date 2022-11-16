class AnalisisDatos:

    def __init__(self, arregloRayos):
        self.arregloRayos = arregloRayos

    def cambiarArreglo(self, nuevoArreglo):
        self.arregloRayos = nuevoArreglo

    def encuentraMaximos(self, sumas):
        maximos = 0
        for i in sumas:
            if(sumas[i] >= 0 and sumas[i+1] < 0):
                maximos = maximos + 1
        return maximos

    def analizaArreglo(self):
        sumas = []
        for i in range(len(self.arregloRayos)):
            for j in range(5):
                if((i+j+1) < len(self.arregloRayos)):
                    sumas[i] += self.arregloRayos[i+j+1] - self.arregloRayos[i+j]
        maximos = self.encuentraMaximos(sumas)
        return maximos


def main():
    arreglo = [1,2,3,4,3,2,1]
    o = AnalisisDatos(arreglo)
    print(o.analizaArreglo)

main()
