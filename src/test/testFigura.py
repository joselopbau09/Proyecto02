import unittest
import os
import sys
import numpy
current_directory = os.path.dirname(__file__)
parent_directory = os.path.split(current_directory)[0]
sys.path.insert(0,parent_directory)
from classes.AnalisisFigura import AnalisisFigura
from classes.GestorImagen import GestorImagen

class testFigura(unittest.TestCase):
    """ Clase que se encarga de realizar las pruebas unitarias de la clase AnalisisFigura.

    Métodos:
    crearAnalisiFigura(self):
        Crea una instancia de la clase.
    testBuscadorCentro(self):
        Prueba para el método BuscadorCentro.
    testCalculaHipotenusa(self):
        Prueba para el método calculaHipotenusa.
    testDentro(self):
        Prueba para el método dentro.
    testRayos(self):
        Prueba para el método rayos.
    """
    def crearAnalisiFigura(self):
        """
        Función que crea las condiciones necesarias para hacer las pruebas sobre las
        funciones de las clase AnalisisFigura.

        Regresa:
            af (Instancia de AnalisisFiguras)
        """
        absolute_folder_path = os.path.dirname(os.path.realpath(__file__))
        absolute_image_path = os.path.join(absolute_folder_path, '../assets/example_1.bmp')
        gi = GestorImagen(absolute_image_path)
        gi.separadorFiguras()
        figuras = gi.obtenerAlmacenador()
        imagen1 = figuras.pop(1)
        arregloImagen = numpy.array(imagen1)
        af = AnalisisFigura(arregloImagen.tolist())
        return af

    def testBuscadorCentro(self):
        """
        Prueba para el método buscadorCentro.
        """
        af = self.crearAnalisiFigura()
        centro_x, centro_y = af.buscadorCentro()
        self.assertGreater(centro_x,0)
        self.assertGreater(centro_y,0)
        imagen = af.obtenerImagen()
        mitad_y = int(len(imagen) / 2)
        mitad_x = int(len(imagen[0]) / 2)
        self.assertTrue((mitad_x <= int(centro_x)) and (int(centro_x) < mitad_x + 10))
        self.assertTrue((mitad_y <= int(centro_y)) and (int(centro_y) < mitad_y + 10))

    def testCalculaHipotenusa(self):
        """
        Prueba para el método calculaHipotenusa.
        """
        af = self.crearAnalisiFigura()
        hipotenusa = af.calculaHipotenusa()
        self.assertGreater(hipotenusa,0)
        imagen = af.obtenerImagen()
        mitad_y = int(len(imagen) / 2)
        mitad_x = int(len(imagen[0]) / 2)
        mitad = min(mitad_x, mitad_y)
        self.assertLess(hipotenusa,mitad)

    def testDentro(self):
        """
        Prueba para el método dentro.
        """
        af = self.crearAnalisiFigura()
        coord_x = 0
        coord_y = 0
        self.assertFalse(af.dentro(coord_x,coord_y))
        coord_x, coord_y = af.buscadorCentro()
        self.assertTrue(af.dentro(coord_x,coord_y))
        h = af.calculaHipotenusa()
        self.assertTrue(af.dentro(coord_x + (h/2),coord_y + (h/2)))
        self.assertFalse(af.dentro(coord_x + h,coord_y + h))

    def testRayos(self):
        """
        Prueba para el método rayos.
        """
        af = self.crearAnalisiFigura()
        centro_x, centro_y = af.buscadorCentro()
        h = af.calculaHipotenusa()
        arregloRayos = af.rayos(centro_x, centro_y, h)
        self.assertEqual(len(arregloRayos),360)
        rayo = arregloRayos[0]
        self.assertAlmostEqual(rayo, h+1)

if __name__ == '__main__':
    unittest.main()