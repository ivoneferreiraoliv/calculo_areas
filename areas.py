"""

Módulo criado para utilizar no programa que calcula a área de figuras planas, usei o "def" para definir cada
função presente neste código.

"""

import math

def area_quadrado(L):
    area = L ** 2
    return print('A área do quadrado é: ', area)
""" Calcula a área de um quadrado """


def area_circulo(R):
    area = math.pi * R ** 2
    return print('A área do círculo é %.3f ' % area)
"""Calcula a área de um círculo"""

def area_triangulo(b, h):
    area = b * h / 2
    return print('A área do triângulo é: ', area)
"""Calcula a área de um triângulo"""

def area_trapezio(B, b, h):
    area = (B + b) * h / 2
    return print('A área do trapézio é: ', area)
"""Calcula a área de um trapézio"""

def area_retangulo(b, h):
    area = b * h
    return print('A área do retângulo é: ', area)
"""Calcula a área de um retângulo"""

def area_losango(h,i):
    area = h * i /2
    return print('A área do losango é: ', area)
"""Calcula a área de um losango"""
