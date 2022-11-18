
import unittest
from classes.GestorImagen import GestorImagen

class testGestor(unittest.TestCase):
    """ Clase que se encarga de realizar las pruebas unitarias de la clase GestorImagen.
    
    """

    def testBuscadorColores(self):
        """ Prueba si la obtención de los colores de las imagen se realiza correctamente.
        
        """
        imagen1 = GestorImagen('assets/example_1.bmp')
        coloresImagen1 = [[164, 159, 150], [123, 106, 78], [200, 165, 102], [150, 92, 50]]
        self.assertListEqual(imagen1.buscadorColoresImagen(), coloresImagen1)
        
        imagen2 = GestorImagen('assets/example_2.bmp')
        coloresImagen2 = [[219, 223, 149], [94, 205, 43], [241, 160, 21], [52, 70, 228], [255, 58, 58], [34, 165, 241], [255, 49, 136], [181, 52, 228]]
        self.assertListEqual(imagen2.buscadorColoresImagen(), coloresImagen2)
        
        imagen3 = GestorImagen('assets/example_3.bmp')
        coloresImagen3 = [[232, 118, 202], [251, 242, 54], [255, 76, 114], [199, 54, 251]]
        self.assertListEqual(imagen3.buscadorColoresImagen(), coloresImagen3)
        
        imagen4 = GestorImagen('assets/example_4.bmp')
        coloresImagen4 = [[111, 187, 127], [119, 111, 187], [165, 232, 90], [90, 232, 165], [90, 150, 232]]
        self.assertListEqual(imagen4.buscadorColoresImagen(), coloresImagen4)

        imagen5 = GestorImagen('assets/example_5.bmp')
        coloresImagen5 = [[90, 195, 232], [13, 86, 187], [69, 116, 219], [90, 135, 232], [116, 69, 219], [159, 13, 187], [47, 231, 241]]
        self.assertListEqual(imagen5.buscadorColoresImagen(), coloresImagen5)

    def testSeparadorFiguras(self):
        pass
    