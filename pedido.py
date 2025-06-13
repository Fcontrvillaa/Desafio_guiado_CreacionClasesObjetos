

from te import Te


print("1. elige el sabor de te 1.negro / 2.verde / 3.hierbas")

sabor =input("elige un sabor : ")

print ("2. elige el formato (300 o 500) :")

formato = int(input("elige formato :  "))

nombre, tiempo, recomendacion = Te.receta(sabor)

