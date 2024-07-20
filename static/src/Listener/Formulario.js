import { creaLaberinto } from '../Laberinto.js';

let matrix = undefined;
let socket = io();
let iniciable = true;

const dimensiones = (e) => {
  if (e.target.value < 3) e.target.value = 3;
}

document.querySelector('#form-row').addEventListener('blur', dimensiones);
document.querySelector('#form-col').addEventListener('blur', dimensiones);
document.querySelector('#formulario').addEventListener('submit', (e) => {
  if (e.target.renglones.value === '') e.target.renglones.value = 5;
  if (e.target.columnas.value === '') e.target.columnas.value = 5;
  e.preventDefault()
  let form = new FormData(e.target);
  form = Object.fromEntries(form.entries());
  matrix = creaLaberinto(form);
  iniciable = true;
});

document.querySelector('#btn-iniciar').addEventListener('click', (e) => {
  if (!matrix) return;
  if (!iniciable) return;
  if (!socket.connected) socket.connect(`http://${document.domain}:${location.port}`);
  socket.emit('crear', {'renglones': matrix.length,
                        'columnas': matrix[0].length,
                        'algoritmo': e.target.closest('.formulario').algoritmo.value});
});

socket.on('reiniciar', (datos) => {
  let inicio = matrix[datos.inicio[0]][datos.inicio[1]];
  inicio.childNodes[1].style['background-color'] = 'darkviolet';
  inicio.classList.add('visitado');
  let meta = matrix[datos.meta[0]][datos.meta[1]];
  meta.childNodes[1].style['background-color'] = 'green';
  iniciable = false;
});

socket.on('mueve', (datos) => {
  matrix[datos.i][datos.j].classList.add('visitado');
});

socket.on('terminado', (dato) => {
  socket.disconnect();
  alert(`Numero de iteraciones: ${dato.iteracion}`);
});
