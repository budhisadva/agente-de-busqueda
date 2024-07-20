from math import sqrt

def euclidiana(actual, meta):
    x1, y1 = actual
    x2, y2 = meta
    return sqrt(pow(x2-x1,2)+pow(y2-y1,2))
