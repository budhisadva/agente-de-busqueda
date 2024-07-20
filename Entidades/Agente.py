class Agente:
    """Agente."""
    def __init__(self, laberinto):
        self.S = self.crea_estados(laberinto)
        self.A = ['R', 'D', 'U', 'L']
        self.s0 = (0,0)
        self.F = laberinto.meta
        self.actual = self.s0

    def __str__(self):
        return str(self.actual)

    def crea_estados(self, laberinto):
        x, y = laberinto.dimensiones()
        estados = []
        for i in range(x):
            for j in range(y):
                estados.append((i,j))
        return estados

    def T(self, s, a):
        i, j = s
        if a == 'L':
            estado = (i, j-1)
        if a == 'R':
            estado = (i, j+1)
        if a == 'D':
            estado = (i+1, j)
        if a == 'U':
            estado = (i-1, j)
        if estado in self.S:
            return estado
        return None

    def set_inicio(self,inicio):
        self.s0 = inicio

    def set_meta(self, meta):
        self.F = meta
