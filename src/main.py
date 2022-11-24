
from sys import argv
from classes.AnalisisFigura import AnalisisFigura
from classes.DetectorVertices import DetectorVertices
from classes.GestorImagen import GestorImagen

class main:

    def conversorHexa(red, green, blue):
        """ Metodo que se encarga realizar la converción de RGB a Hex.

        Parámetros:
            red(int): Cantidad de color rojo.
            green(int): Cantidad de color verde.
            blue(int):  Cantidad de color azul.

        Regresa: str: Color en notación Hex.
   
        """
        return ('{:X}{:X}{:X}').format(red, green, blue)


    script, imagen = argv
    nombreImagen = "assets/%s"%imagen
    gestorImagen = GestorImagen(nombreImagen)
    figuras = gestorImagen.obtenerAlmacenador()
    colores = gestorImagen.obtenerColores()
    total = len(figuras) - 1
    i = 0

    while (i <= total):

        imagen = figuras.pop(0)
        analisisDatos = AnalisisFigura(imagen)

        centro_x, centro_y = analisisDatos.buscadorCentro()
        hipotenusa = analisisDatos.calculaHipotenusa()
        arregloRayos = analisisDatos.rayos(centro_x, centro_y, hipotenusa)

        encontrarVertices = DetectorVertices(arregloRayos)
        vertices2 = encontrarVertices.suavizaDistancias()
        vertices = encontrarVertices.detectaVertices()
        
        colorFigura = colores.pop(0)
        formatoHexa = conversorHexa(colorFigura[0],colorFigura[1],colorFigura[2])

        print(f'{formatoHexa}: {encontrarVertices.clasificaFigura(vertices)}')
        i += 1        


