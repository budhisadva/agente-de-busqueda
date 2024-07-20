import numpy as np

class Laberinto:
    """Laberinto."""
    def __init__(self, renglones=3, columnas=3):
        self.matriz = self.crear_matriz(renglones, columnas)
        self.meta = (renglones-1, columnas-1)

    def __str__(self):
        return str(np.array(self.matriz))

    def crear_matriz(self, renglones, columnas):
        M = [[0 for _ in range(columnas)] for _ in range(renglones)]
        return M

    def dimensiones(self):
        return (len(self.matriz), len(self.matriz[0]))

    def actualiza(self, agente):
        i,j = agente.actual
        self.matriz[i][j] = 1
        i,j = agente.F
        self.matriz[i][j] = 2
