/**
 * Flight tracking simulation
 * --------------------------
 * This script generates random flights and simulates their state transitions
 * from DEPARTING to ON TIME, DELAYED, and ARRIVED. It updates every 10 seconds.
 */

/** @type {Array<Object>} Array containing all active flight objects */
let voli = [];

/** @type {number} Auto-incrementing unique ID for each flight */
let idVolo = 0;

/**
 * Creates a new flight object with initial state 'DEPARTING',
 * assigning a random scheduled time and estimated arrival time.
 * @returns {{
 *   id: number,
 *   nome: string,
 *   da: string,
 *   orario: Date,
 *   stima: Date,
 *   stato: string,
 *   creato: number
 * }} A new flight object
 */
function nuovoVolo() {
  let ora = new Date();
  let previsto = new Date(ora.getTime() + Math.random() * 300000); // now + up to 5 min
  let stimato = new Date(previsto.getTime() + Math.random() * 120000); // + up to 2 min

  return {
    id: idVolo++,
    nome: 'AZ' + Math.floor(100 + Math.random() * 900),
    da: ['Rome', 'Paris', 'London', 'Madrid'][Math.floor(Math.random() * 4)],
    orario: previsto,
    stima: stimato,
    stato: 'DEPARTING',
    creato: Date.now()
  };
}

/**
 * Updates the status of a flight based on its current state:
 * - 'DEPARTING' → 'ON TIME'
 * - 'ON TIME' → 'DELAYED' or 'ARRIVED' (random chance)
 * - 'DELAYED' → 'ARRIVED'
 * The estimated arrival time is extended if the flight becomes delayed.
 * @param {{
 *   stato: string,
 *   stima: Date
 * }} volo The flight object to update
 */
function aggiornaStato(volo) {
  switch (volo.stato) {
    case 'DEPARTING':
      volo.stato = 'ON TIME';
      break;

    case 'ON TIME':
      if (Math.random() > 0.7) {
        volo.stato = 'DELAYED';
        volo.stima = new Date(volo.stima.getTime() + Math.random() * 60000); // add up to 1 min
      } else {
        volo.stato = 'ARRIVED';
      }
      break;

    case 'DELAYED':
      volo.stato = 'ARRIVED';
      break;

    case 'ARRIVED':
      // no further update
      break;
  }
}

/**
 * Renders the flight table inside the element with ID 'lista-voli'.
 * Flights marked as 'DELAYED' get a specific CSS class for styling.
 */
function disegnaTabella() {
  let corpo = document.getElementById('lista-voli');
  corpo.innerHTML = '';

  voli.forEach(v => {
    let riga = document.createElement('tr');
    let statoClass = v.stato === 'DELAYED' ? 'delayed' : '';
    riga.innerHTML = `
      <td>${v.nome}</td>
      <td>${v.da}</td>
      <td>${v.orario.toLocaleTimeString()}</td>
      <td>${v.stima.toLocaleTimeString()}</td>
      <td class="${statoClass}">${v.stato}</td>
    `;
    corpo.appendChild(riga);
  });
}

/**
 * Adds a new flight, updates all flight states, removes old flights,
 * and redraws the flight table. Called every 10 seconds.
 */
function aggiornaLista() {
  voli.push(nuovoVolo());

  for (let i = 0; i < voli.length; i++) {
    aggiornaStato(voli[i]);
  }

  voli = voli.filter(v => {
    return !(v.stato === 'ARRIVED' && Date.now() - v.creato > 60000);
  });

  disegnaTabella();
}

// Initial setup and periodic update every 10 seconds
aggiornaLista();
setInterval(aggiornaLista, 10000);
