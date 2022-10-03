import time
import random


# Realizar un laberinto de 7 filas * 8 columnas y 30 paredes


numero_filas = 7#int(input('Introduzca el número de filas del laberinto: '))
numero_columnas = 8#int(input('Introduzca el número de columnas del laberinto: '))
numero_paredes = 30#int(input('Introduzca el número de paredes del laberinto: '))
numero_espacios = numero_filas * numero_columnas - numero_paredes


def crear_mapa_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios):
    # Se crea un mapa lleno de paredes
    mapa_laberinto = []
    numero_paredes_generadas = 0

    for fila in range(0, numero_filas):
        fila_mapa_laberinto = []
        for columna in range(0, numero_columnas):
            #             if (random.randrange(2) == 1 and numero_paredes_generadas < numero_paredes):
            #                 fila_mapa_laberinto.append('#')
            #                 numero_paredes_generadas += 1
            #             else:
            #                 fila_mapa_laberinto.append(' ')
            fila_mapa_laberinto.append('#')
        mapa_laberinto.append(fila_mapa_laberinto)

    # Se ubica aleatoriamente un punto de inicio y a partir de ese punto se llenan espacios
    par = 0
    numero_espacios_generados = 0
    fila_posicion_actual = random.randrange(numero_filas)
    columna_posicion_actual = random.randrange(numero_columnas)
    mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = '  '
    mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = 'F'

    numero_espacios_generados += 1

    while numero_espacios_generados < numero_espacios:
        direccion = random.randrange(4)
        if direccion == 0 and fila_posicion_actual > 0:
            fila_posicion_actual -= 1
        elif direccion == 1 and fila_posicion_actual < numero_filas - 1:
            fila_posicion_actual += 1
        elif direccion == 2 and columna_posicion_actual > 0:
            columna_posicion_actual -= 1
        else:
            if columna_posicion_actual < numero_columnas - 1:
                columna_posicion_actual += 1
        if fila_posicion_actual > 0 and fila_posicion_actual < numero_filas-1 and columna_posicion_actual > 0 and columna_posicion_actual < numero_columnas-1:
            if mapa_laberinto[fila_posicion_actual][columna_posicion_actual] == '#':
                mapa_laberinto[fila_posicion_actual][columna_posicion_actual] = '  '
                numero_espacios_generados += 1

    return mapa_laberinto



map_laberinto = crear_mapa_laberinto(numero_filas, numero_columnas, numero_paredes, numero_espacios)

#ALTERNATIVA MANUAL

# map_laberinto =  [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'],
#                                 ['#', '  ', '  ', '#', '  ', '#', '  ', '  ', '#', '#', '  ', '  ', '  ', '#', '  ', '  ', '  ', '  ', '  ', '#'],
#                                 ['#', '  ', '  ', '#', '  ', '#', '  ', '  ', '  ', '  ', '  ', '  ', '  ', '#', '  ', '#', '  ', '#', '  ', '#'],
#                                 ['#', '  ', '  ', '#', '  ', '#', '  ', '#', '  ', '  ', '#', '  ', '  ', '#', '  ', '#', '  ', '#', '  ', '#'],
#                                 ['#', '  ', '  ', '#', '  ', '#', '  ', '#', '  ', '  ', '#', '  ', '  ', '  ', '  ', '#', '  ', '#', '#', '#'],
#                                 ['#', '  ', '  ', '#', '  ', '  ', '  ', '#', '  ', '#', '#', '#', '  ', '  ', '  ', '#', '  ', '  ', '#', '#'],
#                                 ['#', '  ', '#', '#', '  ', '  ', '  ', '#', '  ', '#', '#', '  ', '  ', '  ', '  ', '#', '  ', '#', '#', '#'],
#                                 ['#', '  ', '#', '#', '  ', '  ', '  ', '#', '  ', '#', '#', '  ', '  ', '  ', '  ', '#', '  ', '  ', '#', '#'],
#                                 ['#', '  ', '#', '#', '  ', '  ', '  ', '#', '  ', '  ', '#', '#', '  ', '  ', '  ', '#', '  ', '  ', '  ', '#'],
#                                 ['#', '  ', '  ', '#', '  ', '  ', '#', '#', '  ', '  ', '#', '  ', '  ', '  ', '  ', '#', '  ', '  ', '  ', '#'],
#                                 ['#', '  ', '  ', '#', '  ', '#', '#', '#', '  ', '  ', '#', '#', '#', '#', '  ', '#', '  ', '  ', '#', '#'],
#                                 ['#', '  ', '  ', '#', '  ', '#', '#', '#', '  ', '  ', '#', '  ', '  ', '  ', '  ', '#', '  ', '  ', '  ', '#'],
#                                 ['#', '  ', '  ', '#', '  ', '  ', '#', '#', '  ', '  ', '#', '#', '  ', '  ', '  ', '#', '  ', '  ', '#', '#'],
#                                 ['#', '#', '  ', '#', '  ', '  ', '  ', '#', '  ', '  ', '#', '#', '  ', '#', '  ', '#', '  ', '  ', '#', '#'],
#                                 ['#', '  ', '  ', '#', '  ', '  ', '  ', '#', '  ', '  ', '#', '#', '  ', '#', '  ', '#', '  ', '#', '#', '#'],
#                                 ['#', '#', '  ', '#', '  ', '  ', '  ', '#', '  ', '  ', '#', '#', '  ', '#', '  ', '#', '  ', '  ', '#', '#'],
#                                 ['#', '#', '  ', '  ', '  ', '#', '  ', '#', '  ', '  ', '#', '#', '  ', '  ', '#', '#', '#', '  ', '#', '#'],
#                                 ['#', '  ', '  ', '#', '  ', '#', '  ', '#', '  ', '  ', '#', '#', '  ', '  ', '#', '#', '#', '  ', '#', '#'],
#                                 ['#', '  ', '#', '#', '  ', '#', '  ', '#', '  ', '  ', '#', '  ', '  ', '  ', '#', '#', '#', '  ', '  ', 'F'],
#                                 ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']]



class Laberinto:
    def __int__(self, map_laberinto):
        self.resultado = False
#IMPRIMIR LABERINTO
    def imprimirLaberinto(self):

        for i in map_laberinto:
            print(i)
        time.sleep(1)
#MOVIMIENTO DEL JUGADOR
    def paso(self, x, y):
        #rF representa el caracter final
        if map_laberinto[x][y] == 'F':
            return True
        if map_laberinto[x][y] == '#' or map_laberinto[x][y] == '*' :
            return False

        map_laberinto[x][y] = '*'
        self.imprimirLaberinto()
        self.resultado = self.paso(x, y + 1)
        if self.resultado:
            return True
        self.resultado = self.paso(x-1, y)
        if self.resultado:
            return True
        self.resultado = self.paso(x, y - 1)
        if self.resultado:
            return True
        self.resultado = self.paso(x + 1, y )
        if self.resultado:
            return True

        map_laberinto[x][y] = '  '
        self.imprimirLaberinto()
        return False

#LLAMAR ALOS METODOS
laberinto = Laberinto()
laberinto.paso(2, 2)
print(" ")
print("el objeto o caracter llego al  fin del laberinto")
