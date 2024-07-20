let matrix = undefined;

const creaMatriz = (args) => {
  matrix = new Array(Number(args.renglones)).fill(0);
  for (let i = 0; i < args.renglones; i++) {
    matrix[i] = new Array(Number(args.columnas)).fill(0);
  }
}

const creaInterfaz = (args) => {
  if (!matrix) return;
  let laberinto = document.querySelector('.laberinto');
  laberinto.style['grid-template-columns'] = `repeat(${args.columnas}, 1fr)`;
  laberinto.style['grid-template-rows'] = `repeat(${args.renglones}, 1fr)`;
  laberinto.innerHTML = '';
  for (let i = 0; i < matrix.length; i++) {
    for (let j = 0; j < matrix[0].length; j++) {
      let carta = document.createElement('div');
      let frente = document.createElement('div');
      let dorso = document.createElement('div');
      carta.classList.add('carta');
      frente.classList.add('frente');
      dorso.classList.add('dorso');
      carta.appendChild(frente);
      carta.appendChild(dorso);
      laberinto.appendChild(carta);
      matrix[i][j] = carta;
    }
  }
}

const creaLaberinto = (args) => {
  creaMatriz(args);
  creaInterfaz(args);
  return matrix;
}

export { creaLaberinto };
