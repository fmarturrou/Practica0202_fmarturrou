producto = input("Escribe el nombre de un producto:\n")
precio = float(input("Introduce el precio de una unidad:\n"))
unidades = int(input("Introduce el número de unidades:\n"))
total = (precio*unidades)
print("El producto {} vale {:9.2f}€ y quiero {:3d} unidades, el coste total es de {:11.2f}€".format(producto,precio,unidades,total))
#lo de que salen 6 digitos y 2 decimales se hace con la función {:n:mf}, donde n es el número
#de enteros que se quiere que se vean y la m es el número de decimales que se quiere que se vean
#y el {:nd} es para que aparezcan 6 digitos pero sin decimales, en este caso como queríamos 3 digitos
#introducimos {:3d}