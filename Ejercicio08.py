NG313 = (input("Dime el precio del producto que quieras con 2 decimales:\n"))
print("El precio es de", NG313[:NG313.find(".")], "euros y", NG313[NG313.find(".")+1:], "centimos")