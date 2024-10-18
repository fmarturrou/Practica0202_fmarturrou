NL273 = input("Introduce una fecha en formato dd/mm/aaaa\n")
SD200 = NL273[:NL273.find('/')]
ND202 = NL273[NL273.find('/')+1:]
N310UA = ND202[:ND202.find('/')]
N280UB = ND202[ND202.find('/')+1:]
print('Día', SD200)
print('Mes', N310UA)
print('Año', N280UB)