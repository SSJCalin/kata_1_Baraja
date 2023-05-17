import random


def crear_baraja(numeros, palos):
    # Crear la baraja completa
    baraja = []
    palos = ['o', 'c', 'e', 'b']
    numeros = ['A', '1', '2', '3', '4', '5', '6', '7', 'S', 'C', 'R']

    for palo in palos:
        for numero in numeros:
            carta = palo + numero
            baraja.append(carta)
    return baraja


def barajar_for(baraja):
    # Barajar los naipes
    for i in range(len(baraja)):
        # Generar un índice aleatorio
        j = random.randrange(len(lenbaraja))
        # Intercambiar la posición de la carta actual con la carta en el índice aleatorio
        baraja[i], baraja[j] = baraja[j], baraja[i]
    return baraja
