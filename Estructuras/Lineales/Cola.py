class Cola:
    """ """
    def __init__(self):
        self.cola = []
        self.longitud = 0

    def __str__(self):
        return str(self.cola)

    def empty(self):
        return self.longitud == 0

    def queue(self, item):
        self.cola.append(item)
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
