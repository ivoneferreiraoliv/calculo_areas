"""
Aqui apliquei o meu módulo que calcula áreas e mudei o método de escolha das figuras, achei que assim
ficaria mais legal e intuitivo.

"""



import areas

print("Calcular Áreas de figuras geométricas.\n")
print("1.Quadrado.\n2.Círculo.\n3.Triângulo.\n4.Trapézio.\n5.Retângulo.\n6.Losango.\n")

x = float(input("Escolha uma figura: "))

if x == 1:
    L = float(input('Insira o lado: '))
    areas.area_quadrado(L)

if x == 2:
    R = float(input('Insira o raio do círculo: '))
    areas.area_circulo(R)

if x == 3:
    b = float(input('Insira a base: '))
    h = float(input('Insira a altura: '))
    areas.area_triangulo(b, h)

if x == 4:
    B = float(input('Insira a base 1:'))
    b = float(input('Insira a base 2: '))
    h = float(input('Insira a altura: '))
    areas.area_trapezio(B, b, h)

if x == 5:
    b = float(input('Insira a base: '))
    h = float(input('Insira a altura: '))
    areas.area_retangulo(b, h)

if x == 6:
    h = float(input('Tamanho da diagonal:'))
    i = float(input('Tamanho da outra diagonal:'))
    areas.area_losango(h,i)
