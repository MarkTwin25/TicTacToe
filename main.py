class Juego:

    def __init__(self):
        self.tablero = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.jugador1 = "X"
        self.jugador2 = "O"

    def imprimir_tablero(self):
        for i in range(len(self.tablero)):
            print(f"{self.tablero[i][0]} | {self.tablero[i][1]} | {self.tablero[i][2]}")
            if i < len(self.tablero)-1:
                print("- - - - -")

    def tirar(self, jugador, fila, columna):
        while fila >2 or fila <0 or columna > 2 or columna < 0:
            print("Intentalo de nuevo! fila: 1-3, columna: 1-3")
            fila = int(input("Fila: "))
            columna = int(input("Columna: "))

        while self.tablero[fila][columna] == "X" or self.tablero[fila][columna] == "O":
            print("Intentalo de nuevo! Casilla ya ocupada!")
            fila = int(input("Fila: "))
            columna = int(input("Columna: "))

        self.tablero[fila][columna] = jugador

    def revisar_ganador(self,jugador):
        casos_ganadores = [self.tablero[0], self.tablero[1], self.tablero[2],
                         [self.tablero[0][0], self.tablero[1][0], self.tablero[2][0]],
                         [self.tablero[0][1], self.tablero[1][1], self.tablero[2][1]],
                         [self.tablero[0][2], self.tablero[1][2], self.tablero[2][2]],
                         [self.tablero[0][0], self.tablero[1][1], self.tablero[2][2]],
                         [self.tablero[2][0], self.tablero[1][1], self.tablero[0][2]]
                          ]

        for i in casos_ganadores:
            if len(list(filter(lambda x:x == jugador,i))) == 3:
                self.imprimir_tablero()

                print(f"----- Ganador: {jugador} ------")
                return True
        return False

    def partida(self):
        count = 0
        ganador = False
        while count <9 and ganador == False:
            self.imprimir_tablero()
            print("Jugador 1: ")
            fila = int(input("Fila: "))
            columna = int(input("Columna: "))
            self.tirar(self.jugador1, fila-1, columna-1)
            count+=1
            ganador = self.revisar_ganador(self.jugador1)
            if ganador == False and count <=8:
                self.imprimir_tablero()
                print("Jugador 2: ")
                fila = int(input("Fila: "))
                columna = int(input("Columna: "))
                self.tirar(self.jugador2,fila-1,columna-1)
                count+=1
                ganador = self.revisar_ganador(self.jugador2)
        if ganador == False:
            self.imprimir_tablero()
            print("Empate!")

if __name__ == "__main__":
    Juego().partida()
