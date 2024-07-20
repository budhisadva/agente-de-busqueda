class Pila:
    """ """
    def __init__(self):
        self.pila = []
        self.longitud = 0

    def __str__(self):
        return str(self.pila)

    def empty(self):
        return self.longitud == 0

    def pop(self):
        if self.empty():
            return None
        item = self.pila.pop(self.longitud-1)
        self.longitud -= 1
        return item

    def push(self, item):
        self.pila.append(item)
        self.longitud += 1

    def peek(self):
        if self.empty():
            return None
        return self.pila[self.longitud-1]
