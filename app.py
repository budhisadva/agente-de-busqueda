from flask_socketio import SocketIO, emit
from flask import Flask, render_template
from time import sleep
import os
from Estructuras.Lineales.ColaPrioridades import ColaPrioridades
from Estructuras.Lineales.Cola import Cola
from Estructuras.Lineales.Pila import Pila
from General.Heuristicas import euclidiana
from General.funciones import genera_coor
from Entidades.Laberinto import Laberinto
from Entidades.Agente import Agente

app = Flask(__name__)
app.config.from_mapping(
    FLASK_DEBUG=os.environ.get('FLASK_DEBUG'),
    SECRET_KEY=os.environ.get('SECRET_KEY')
)
socket = SocketIO(app)

@app.route("/")
def index():
    return render_template('index.html')

@socket.on('connect')
def conecta():
    print('WebSocket conectado')

@socket.on('disconnect')
def desconecta():
    print('WebSocket desconectado')

@socket.on('crear')
def recibeMensaje(dato):
    sleep(1)
    laberinto = Laberinto(dato['renglones'], dato['columnas'])
    i, j = laberinto.dimensiones()
    agente = Agente(laberinto)
    agente.set_inicio( genera_coor(i,j) )
    agente.set_meta( genera_coor(i,j) )
    emit('reiniciar', {'inicio': agente.s0, 'meta': agente.F}, broadcast=True)
    match dato['algoritmo']:
        case 'bfs':
            bfs(agente)
        case 'dfs':
            dfs(agente)
        case 'greedy':
            primero_ambicioso(agente)
        case _:
            pass

def bfs(agente):
    visitados = [agente.s0]
    cola = Cola()
    cola.queue(agente.s0)
    it = 0
    while not cola.empty() and agente.actual != agente.F:
        agente.actual = cola.dequeue()
        for accion in agente.A:
            vecino = agente.T(agente.actual, accion)
            if vecino is not None and vecino not in visitados:
                cola.queue(vecino)
                visitados.append(vecino)
        i,j = agente.actual
        emit('mueve', {'i': i, 'j':j}, broadcast=True)
        sleep(.1)
        it += 1
    emit('terminado', {'iteracion': it}, broadcast=True)

def dfs(agente):
    visitados = [agente.s0]
    pila = Pila()
    pila.push(agente.s0)
    it = 0
    while not pila.empty() and agente.actual != agente.F:
        agente.actual = pila.pop()
        for accion in agente.A:
            vecino = agente.T(agente.actual, accion)
            if vecino is not None and vecino not in visitados:
                pila.push(vecino)
                visitados.append(vecino)
        i,j = agente.actual
        emit('mueve', {'i': i, 'j':j}, broadcast=True)
        sleep(.1)
        it += 1
    emit('terminado', {'iteracion': it}, broadcast=True)

def primero_ambicioso(agente):
    visitados = []
    frontera = ColaPrioridades()
    frontera.queue({"actual":agente.s0, "meta":agente.F}, euclidiana)
    it = 0
    while not frontera.empty() and agente.actual != agente.F:
        actual = frontera.dequeue()
        visitados.append(actual[0])
        agente.actual = actual[0]
        for accion in agente.A:
            vecino = agente.T(agente.actual, accion)
            if vecino is not None and vecino not in visitados:
                frontera.queue({"actual":vecino, "meta":agente.F}, euclidiana)
        i,j = agente.actual
        emit('mueve', {'i': i, 'j':j}, broadcast=True)
        sleep(.2)
        it += 1
    emit('terminado', {'iteracion': it}, broadcast=True)
