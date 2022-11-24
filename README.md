### Integrantes
- García Velasco Erick Iram  - 318044309
- López Bautista José Luis - 317191895
- Eduardo Alfonso Reyes López - 420003681
# Identificador de figuras 

Programa que identifica las figuras dentro de una imagen según su número de vértices.

## Versión o herramientas:

Paqueterias usadas:
- [Numpy](https://numpy.org/)
- [Pillow](https://python-pillow.org/)

## Requerimentos
Para ejecutar el programa se necesita:
- [Python 3] (https://www.python.org/downloads)
- Instalar la paquetería Pillow, se puede hacer con el siguiente comando: 
```
python3 -m pip install --upgrade pip
```
Luego se ejecuta:
```
python3 -m pip install --upgrade Pillow
```
- Instalar la paquetería Numpy:
```
pip install numpy
```

## Cómo ejecutarlo:
1. Dirigirse en la terminal a la carpeta donde está ubicado el archivo llamado `main.py` el cual esta en la carpeta src, y por la entrada estandar agrega el nombre de la imagen: 
```
Proyecto-02\src>
```
2. Recuerda que se debe de agregar la imagen a la carpeta assets, una vez hecho esto se escribe el siguiente comando y posterior a `main.py` se ecribe el nombre de la imagen y se ejecuta el comando.

```
Python3 main.py
```

-Ejemplo:

```
Python3 main.py example_1.bmp
```

-Para ejecutar las pruebas unitarias desde la misma posición en el directorio ejecutar el siguiente comando:

```
python3 -m unittest discover
```

## Cómo usarlo
- Dada una imagen o archivo que implemente file.read, file.seek o file.tell. Si cumple con tener un
color de fondo y colores de figuras homogéneas distintos entre si, el programa al ejecutarse 
regresará en consola la clasificación de las figuras presentes en la imagen en 4 categorías: 
círculo (O), triángulo (T), cuadrilátero (C) u otros (X) junto con su color en hexadecimal.

## Bibliotecas usadas
- sys
- PIL
- copy
- numpy
- math

## Entornos donde fue probado
- Windows 10
- Ubuntu 22.04.1
