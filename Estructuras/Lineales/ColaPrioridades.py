class ColaPrioridades:
    """ """
    def __init__(self):
        self.cola = []
        self.longitud = 0

    def __str__(self):
        return str(self.cola)

    def empty(self):
        return self.longitud == 0

    def queue(self, coordenadas, h):
        distancia = h(coordenadas['actual'],coordenadas['meta'])
        if self.empty():
            self.cola.append((coordenadas['actual'], distancia))
        else:
            i=0
            while i < self.longitud:
                if distancia<self.cola[i][1]:
                    break
                i+=1
            self.cola.insert(i, (coordenadas['actual'], distancia))
        self.longitud += 1

    def dequeue(self):
        if self.empty():
            return None
        self.longitud -= 1
        return self.cola.pop(0)

    def peek(self):
        if self.empty():
            return None
        return self.cola[0]
