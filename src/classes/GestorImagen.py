from PIL import Image
from numpy import asarray

class GestorImage:

    def __init__(self, imagen):
        self.imagen = imagen
        img = Image.open(f'{imagen}')
        self.matrizImagen = asarray(img)