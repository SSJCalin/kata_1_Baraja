import barajas

"""
print(barajas.crear_baraja(["A", "2", "3"], ("rojos", "verdes")))


b = barajas.crear_baraja("A234567SCR", "oceb")
print(b)
barajas.barajar_for(b)
"""
mi_baraja = barajas.Baraja("A234567SCR", "oceb")
print(mi_baraja.repartir(2, 3))

mi_baraja = barajas.Baraja("A234567SCR", "oceb")
print(mi_baraja.repartir_como_los_niños(2, 3))

