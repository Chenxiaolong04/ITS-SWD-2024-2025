Differenze tra slice(), substring() e substr()

In JavaScript, slice(), substring() e substr() sono metodi utilizzati per estrarre parti di una stringa. Tuttavia, ci sono alcune differenze tra di loro.

1. slice()

Sintassi:

string.slice(start, end)

start: indice di inizio (incluso).

end: indice di fine (escluso, opzionale).

Se end non viene specificato, estrae fino alla fine della stringa.

Supporta indici negativi (conta dalla fine della stringa).

Esempio:

let text = "JavaScript";
console.log(text.slice(0, 4));  // "Java"
console.log(text.slice(-6));   // "Script"

2. substring()

Sintassi:

string.substring(start, end)

start: indice di inizio (incluso).

end: indice di fine (escluso, opzionale).

Se end non viene specificato, estrae fino alla fine della stringa.

Non supporta indici negativi (li considera come 0).

Se start > end, li inverte automaticamente.

Esempio:

let text = "JavaScript";
console.log(text.substring(0, 4));  // "Java"
console.log(text.substring(4, 0));  // "Java" (inverte start e end)

3. substr() (Deprecato)

⚠️ Nota: substr() è stato deprecato e non dovrebbe essere usato nelle nuove versioni di JavaScript.

Sintassi:

string.substr(start, length)

start: indice di inizio (incluso).

length: numero di caratteri da estrarre (opzionale).

Se length non è specificato, estrae fino alla fine della stringa.

Supporta indici negativi (conta dalla fine della stringa).

Esempio:

let text = "JavaScript";
console.log(text.substr(0, 4));  // "Java"
console.log(text.substr(-6, 6)); // "Script"

