-- Esercizi Insert




-- 1. Inserire un singolo record
INSERT INTO prodotti (codice_prodotto, nome_prodotto, colore, taglia, magazzino)
VALUES ('P001', 'Maglietta', 'Rosso', 'M', 'MZ01');

-- 2. Inserire più record in una sola istruzione
INSERT INTO fornitori (codice_fornitore, nome_fornitore, numero_soci, sede)
VALUES 
    ('F001', 'Fornitore A', 3, 'Torino'),
    ('F002', 'Fornitore B', 5, 'Milano'),
    ('F003', 'Fornitore C', 2, 'Roma');

-- 3. Inserire un record parziale
INSERT INTO clienti (codice_cliente, Nome, Email)
VALUES ('C001', 'Mario Rossi', NULL);

-- 4. Inserire un record calcolato da un'altra tabella
INSERT INTO prodotti_archivio (codice_prodotto, nome_prodotto, colore, taglia)
SELECT codice_prodotto, nome_prodotto, colore, taglia FROM prodotti WHERE codice_prodotto = 'P001';

-- 5. Inserire una riga con una sottoquery
INSERT INTO ordini (codice_ordine, codice_cliente, data_ordine)
SELECT 'O001', codice_cliente, CURRENT_DATE
FROM clienti
WHERE data_registrazione = (SELECT MAX(data_registrazione) FROM clienti);

-- 6. Inserire un record con valori default
INSERT INTO fornitori (codice_fornitore, nome_fornitore)
VALUES ('F004', 'Fornitore D');

-- 7. Inserire dati con valori calcolati
INSERT INTO vendite (codice_vendita, codice_prodotto, Quantita, PrezzoUnitario, Totale)
VALUES ('V001', 'P002', 5, 20, 5 * 20);

-- 8. Inserire dati duplicati con modifiche
INSERT INTO prodotti (codice_prodotto, nome_prodotto, colore, taglia, magazzino)
SELECT 'P002', nome_prodotto, 'Blu', taglia, magazzino
FROM prodotti WHERE codice_prodotto = 'P001';

-- 9. Inserire dati nella tabella di associazione
INSERT INTO fornitori_prodotti (codice_fornitore, codice_prodotto, Qta)
VALUES ('F001', 'P003', 100);

-- 10. Inserire dati provenienti da una tabella di log
INSERT INTO ordini (codice_ordine, codice_cliente, data_ordine)
SELECT codice_ordine, codice_cliente, data_ordine FROM ordini_temp;




-- Esercizi di Update



-- 1. Aggiornare il colore dei prodotti con il codice "P001" in "rosso"
UPDATE prodotti
SET colore = 'rosso'
WHERE codice_prodotto = 'P001';

-- 2. Incrementare il numero di soci di tutti i fornitori con sede a "Milano" di 2
UPDATE fornitori
SET numero_soci = numero_soci + 2
WHERE sede = 'Milano';

-- 3. Aggiornare il magazzino del prodotto "P002" a "MZ002"
UPDATE prodotti
SET magazzino = 'MZ002'
WHERE codice_prodotto = 'P002';

-- 4. Ridurre del 10% la quantità disponibile per tutti i prodotti forniti da "F001"
UPDATE fornitori_prodotti
SET Qta = Qta * 0.9
WHERE codice_fornitore = 'F001';

-- 5. Impostare il colore dei prodotti senza un colore definito a "bianco"
UPDATE prodotti
SET colore = 'bianco'
WHERE colore IS NULL;

-- 6. Cambiare l'indirizzo di tutti i fornitori con codice "F002" in "Via Roma, 10"
UPDATE fornitori
SET sede = 'Via Roma, 10'
WHERE codice_fornitore = 'F002';

-- 7. Impostare la quantità a 0 per i prodotti mai forniti da alcun fornitore
UPDATE prodotti
SET magazzino = 'Non fornito'
WHERE codice_prodotto NOT IN (SELECT DISTINCT codice_prodotto FROM fornitori_prodotti);

-- 8. Aggiornare la sede dei fornitori con meno di 3 soci a "Sede Sconosciuta"
UPDATE fornitori
SET sede = 'Sede Sconosciuta'
WHERE numero_soci < 3;

-- 9. Cambiare la taglia di tutti i prodotti di colore "verde" a "L"
UPDATE prodotti
SET taglia = 'L'
WHERE colore = 'verde';

-- 10. Aggiornare il nome dei fornitori che hanno fornito almeno un prodotto con quantità superiore a 100 in "Fornitore Premium"
UPDATE fornitori
SET nome_fornitore = 'Fornitore Premium'
WHERE codice_fornitore IN (
    SELECT codice_fornitore
    FROM fornitori_prodotti
    WHERE Qta > 100
);




-- Esercizi di Delete




-- 1. Eliminare i prodotti con magazzino "MZ003"
DELETE FROM prodotti
WHERE magazzino = 'MZ003';

-- 2. Rimuovere tutti i fornitori con sede a "Napoli"
DELETE FROM fornitori
WHERE sede = 'Napoli';

-- 3. Eliminare tutte le relazioni prodotto-fornitore per il prodotto con codice "P004"
DELETE FROM fornitori_prodotti
WHERE codice_prodotto = 'P004';

-- 4. Rimuovere tutti i prodotti con colore "nero"
DELETE FROM prodotti
WHERE colore = 'nero';

-- 5. Eliminare tutti i fornitori con meno di 5 soci
DELETE FROM fornitori
WHERE numero_soci < 5;

-- 6. Eliminare le relazioni prodotto-fornitore per i fornitori con codice "F003"
DELETE FROM fornitori_prodotti
WHERE codice_fornitore = 'F003';

-- 7. Eliminare tutti i prodotti mai forniti da alcun fornitore
DELETE FROM prodotti
WHERE codice_prodotto NOT IN (SELECT DISTINCT codice_prodotto FROM fornitori_prodotti);

-- 8. Rimuovere tutti i fornitori che non hanno fornito prodotti
DELETE FROM fornitori
WHERE codice_fornitore NOT IN (SELECT DISTINCT codice_fornitore FROM fornitori_prodotti);

-- 9. Eliminare tutti i prodotti con quantità inferiore a 10 in qualsiasi relazione prodotto-fornitore
DELETE FROM fornitori_prodotti
WHERE Qta < 10;

-- 10. Rimuovere tutti i prodotti di taglia "S" e colore "giallo"
DELETE FROM prodotti
WHERE taglia = 'S' AND colore = 'giallo';




-- Esercizi di SELECT




-- 1. Selezionare tutti i dettagli dei prodotti di colore rosso
SELECT * 
FROM prodotti
WHERE colore = 'rosso';

-- 2. Trovare i nomi e le sedi dei fornitori con più di 5 soci
SELECT nome_fornitore, sede
FROM fornitori
WHERE numero_soci > 5;

-- 3. Trovare il nome e l'email dei clienti registrati negli ultimi 30 giorni
SELECT nome, email
FROM clienti
WHERE data_registrazione >= CURRENT_DATE - INTERVAL '30 days';

-- 4. Calcolare il totale delle vendite per ogni prodotto
SELECT codice_prodotto, SUM(totale) AS totale_vendite
FROM vendite
GROUP BY codice_prodotto;

-- 5. Recuperare i dettagli dei fornitori che forniscono almeno un prodotto di colore "verde"
SELECT DISTINCT f.codice_fornitore, f.nome_fornitore, f.sede
FROM fornitori f
JOIN fornitori_prodotti fp ON f.codice_fornitore = fp.codice_fornitore
JOIN prodotti p ON fp.codice_prodotto = p.codice_prodotto
WHERE p.colore = 'verde';

-- 6. Trovare i nomi dei clienti che hanno effettuato ordini
SELECT DISTINCT c.nome
FROM clienti c
JOIN ordini o ON c.codice_cliente = o.codice_cliente;

-- 7. Visualizzare i prodotti mai forniti da alcun fornitore
SELECT p.nome_prodotto
FROM prodotti p
LEFT JOIN fornitori_prodotti fp ON p.codice_prodotto = fp.codice_prodotto
WHERE fp.codice_prodotto IS NULL;

-- 8. Trovare i fornitori che forniscono almeno due prodotti diversi
SELECT codice_fornitore
FROM fornitori_prodotti
GROUP BY codice_fornitore
HAVING COUNT(DISTINCT codice_prodotto) >= 2;

-- 9. Recuperare i dettagli delle vendite per prodotti il cui prezzo unitario è maggiore della media
SELECT *
FROM vendite
WHERE PrezzoUnitario > (SELECT AVG(PrezzoUnitario) FROM vendite);

-- 10. Trovare i prodotti venduti esclusivamente nel magazzino "MZ001"
SELECT p.nome_prodotto
FROM prodotti p
WHERE p.magazzino = 'MZ001'
AND NOT EXISTS (
    SELECT 1
    FROM vendite v
    WHERE v.codice_prodotto = p.codice_prodotto AND p.magazzino != 'MZ001'
);




-- Esercizi Operatori



-- 1. Selezionare il nome e il prezzo aumentato del 10% per tutti i prodotti
SELECT nome_prodotto, PrezzoUnitario * 1.1 AS NuovoPrezzo
FROM prodotti;

-- 2. Trovare i prodotti con un prezzo tra 50 e 100 (inclusi)
SELECT nome_prodotto, PrezzoUnitario
FROM prodotti
WHERE PrezzoUnitario BETWEEN 50 AND 100;

-- 3. Visualizzare i fornitori con un numero di soci maggiore o uguale a 10
SELECT nome_fornitore, numero_soci
FROM fornitori
WHERE numero_soci >= 10;

-- 4. Calcolare la quantità totale fornita per ogni prodotto
SELECT codice_prodotto, SUM(Qta) AS TotaleQuantita
FROM fornitori_prodotti
GROUP BY codice_prodotto;

-- 5. Trovare i fornitori con il nome che inizia con "A"
SELECT nome_fornitore
FROM fornitori
WHERE nome_fornitore LIKE 'A%';

-- 6. Mostrare tutti i prodotti che non sono né rossi né gialli
SELECT nome_prodotto, colore
FROM prodotti
WHERE colore NOT IN ('Rosso', 'Giallo');

-- 7. Trovare i fornitori che si trovano in città diverse da "Milano"
SELECT nome_fornitore, sede
FROM fornitori
WHERE sede <> 'Milano';

-- 8. Calcolare la media delle quantità fornite da ciascun fornitore
SELECT codice_fornitore, AVG(Qta) AS MediaQuantita
FROM fornitori_prodotti
GROUP BY codice_fornitore;

-- 9. Selezionare tutti i fornitori che forniscono almeno un prodotto in quantità superiore a 50
SELECT DISTINCT codice_fornitore
FROM fornitori_prodotti
WHERE Qta > 50;

-- 10. Visualizzare i prodotti con prezzo maggiore di 20 e in magazzini diversi da "MZ001"
SELECT p.nome_prodotto, v.PrezzoUnitario, p.magazzino
FROM prodotti p
JOIN vendite v ON p.codice_prodotto = v.codice_prodotto
WHERE v.PrezzoUnitario > 20 
AND p.magazzino <> 'MZ001';





-- Esercizi con JOIN




-- 1. Mostrare il nome dei prodotti e i nomi dei fornitori che li forniscono
SELECT P.nome_prodotto, F.nome_fornitore
FROM prodotti P
JOIN fornitori_prodotti FP ON P.codice_prodotto = FP.codice_prodotto
JOIN fornitori F ON FP.codice_fornitore = F.codice_fornitore;

-- 2. Trovare i fornitori che non forniscono alcun prodotto
SELECT F.nome_fornitore
FROM fornitori F
LEFT JOIN fornitori_prodotti FP ON F.codice_fornitore = FP.codice_fornitore
WHERE FP.codice_prodotto IS NULL;

-- 3. Calcolare la quantità totale fornita per ogni prodotto, includendo quelli non forniti
SELECT P.nome_prodotto, COALESCE(SUM(FP.Qta), 0) AS totale_quantita
FROM prodotti P
LEFT JOIN fornitori_prodotti FP ON P.codice_prodotto = FP.codice_prodotto
GROUP BY P.codice_prodotto, P.nome_prodotto;

-- 4. Visualizzare i fornitori che forniscono prodotti con quantità maggiore di 50
SELECT F.nome_fornitore, P.nome_prodotto, FP.Qta
FROM fornitori_prodotti FP
JOIN fornitori F ON FP.codice_fornitore = F.codice_fornitore
JOIN prodotti P ON FP.codice_prodotto = P.codice_prodotto
WHERE FP.Qta > 50;

-- 5. Trovare i prodotti non forniti da nessun fornitore
SELECT P.nome_prodotto
FROM prodotti P
LEFT JOIN fornitori_prodotti FP ON P.codice_prodotto = FP.codice_prodotto
WHERE FP.codice_fornitore IS NULL;

-- 6. Trovare i fornitori che forniscono solo prodotti di colore "rosso"
SELECT DISTINCT F.nome_fornitore
FROM fornitori F
JOIN fornitori_prodotti FP ON F.codice_fornitore = FP.codice_fornitore
JOIN prodotti P ON FP.codice_prodotto = P.codice_prodotto
WHERE P.colore = 'rosso'
  AND F.codice_fornitore NOT IN (
      SELECT FP2.codice_fornitore
      FROM fornitori_prodotti FP2
      JOIN prodotti P2 ON FP2.codice_prodotto = P2.codice_prodotto
      WHERE P2.colore <> 'rosso'
  );

-- 7. Visualizzare i fornitori che forniscono almeno due prodotti diversi
SELECT F.nome_fornitore
FROM fornitori F
JOIN fornitori_prodotti FP ON F.codice_fornitore = FP.codice_fornitore
GROUP BY F.codice_fornitore, F.nome_fornitore
HAVING COUNT(DISTINCT FP.codice_prodotto) >= 2;

-- 8. Trovare i prodotti forniti solo da un unico fornitore
SELECT P.nome_prodotto
FROM prodotti P
JOIN fornitori_prodotti FP ON P.codice_prodotto = FP.codice_prodotto
GROUP BY P.codice_prodotto, P.nome_prodotto
HAVING COUNT(DISTINCT FP.codice_fornitore) = 1;

-- 9. Trovare i fornitori che forniscono prodotti con quantità media superiore a 30
SELECT F.nome_fornitore
FROM fornitori F
JOIN fornitori_prodotti FP ON F.codice_fornitore = FP.codice_fornitore
GROUP BY F.codice_fornitore, F.nome_fornitore
HAVING AVG(FP.Qta) > 30;

-- 10. Visualizzare i prodotti e il numero di fornitori che li forniscono
SELECT P.nome_prodotto, COUNT(DISTINCT FP.codice_fornitore) AS numero_fornitori
FROM prodotti P
LEFT JOIN fornitori_prodotti FP ON P.codice_prodotto = FP.codice_prodotto
GROUP BY P.codice_prodotto, P.nome_prodotto;




-- Esercizi con GROUP BY



-- 1. Contare il numero totale di prodotti disponibili
SELECT COUNT(*) AS NumeroProdotti FROM prodotti;

-- 2. Calcolare la quantità totale fornita per ogni prodotto
SELECT p.nome_prodotto, SUM(fp.Qta) AS QuantitaTotale
FROM prodotti p
JOIN fornitori_prodotti fp ON p.codice_prodotto = fp.codice_prodotto
GROUP BY p.codice_prodotto, p.nome_prodotto;

-- 3. Determinare la quantità media di prodotti forniti da ciascun fornitore
SELECT f.nome_fornitore, AVG(fp.Qta) AS QuantitaMedia
FROM fornitori f
JOIN fornitori_prodotti fp ON f.codice_fornitore = fp.codice_fornitore
GROUP BY f.codice_fornitore, f.nome_fornitore;

-- 4. Calcolare il numero di fornitori per ciascun prodotto
SELECT p.nome_prodotto, COUNT(DISTINCT fp.codice_fornitore) AS NumeroFornitori
FROM prodotti p
LEFT JOIN fornitori_prodotti fp ON p.codice_prodotto = fp.codice_prodotto
GROUP BY p.codice_prodotto, p.nome_prodotto;

-- 5. Trovare il prodotto con la quantità massima fornita
SELECT p.nome_prodotto, MAX(fp.Qta) AS QuantitaMassima
FROM prodotti p
JOIN fornitori_prodotti fp ON p.codice_prodotto = fp.codice_prodotto
GROUP BY p.codice_prodotto, p.nome_prodotto
ORDER BY QuantitaMassima DESC
LIMIT 1;

-- 6. Determinare la quantità totale fornita per ciascun colore di prodotto
SELECT p.colore, SUM(fp.Qta) AS QuantitaTotale
FROM prodotti p
JOIN fornitori_prodotti fp ON p.codice_prodotto = fp.codice_prodotto
GROUP BY p.colore;

-- 7. Contare il numero di prodotti forniti da ogni fornitore
SELECT f.nome_fornitore, COUNT(DISTINCT fp.codice_prodotto) AS NumeroProdotti
FROM fornitori f
JOIN fornitori_prodotti fp ON f.codice_fornitore = fp.codice_fornitore
GROUP BY f.codice_fornitore, f.nome_fornitore;

-- 8. Calcolare il numero medio di soci dei fornitori per città
SELECT f.sede, AVG(f.numero_soci) AS NumeroMedioSoci
FROM fornitori f
GROUP BY f.sede;

-- 9. Trovare i prodotti con una quantità totale fornita superiore a 100
SELECT p.nome_prodotto, SUM(fp.Qta) AS QuantitaTotale
FROM prodotti p
JOIN fornitori_prodotti fp ON p.codice_prodotto = fp.codice_prodotto
GROUP BY p.codice_prodotto, p.nome_prodotto
HAVING SUM(fp.Qta) > 100;

-- 10. Determinare il numero di prodotti forniti e la quantità totale fornita da fornitori con più di 5 soci
SELECT f.nome_fornitore, COUNT(DISTINCT fp.codice_prodotto) AS NumeroProdotti, SUM(fp.Qta) AS QuantitaTotale
FROM fornitori f
JOIN fornitori_prodotti fp ON f.codice_fornitore = fp.codice_fornitore
WHERE f.numero_soci > 5
GROUP BY f.codice_fornitore, f.nome_fornitore;




-- Esercizi con funzioni



-- 1. Convertire il testo in maiuscolo
SELECT UPPER(Nome) AS nome_maiuscolo FROM clienti;

-- 2. Convertire il testo in minuscolo
SELECT LOWER(Cognome) AS cognome_minuscolo FROM clienti;

-- 3. Concatenare stringhe
SELECT CONCAT(Nome, ' ', Cognome) AS nome_completo FROM clienti;

-- 4. Estrarre una parte di testo
SELECT Nome, SUBSTRING(Nome, 1, 3) AS abbreviazione FROM clienti;

-- 5. Calcolare la lunghezza di una stringa
SELECT Nome, CHAR_LENGTH(Nome) AS lunghezza FROM clienti;

-- 6. Rimuovere spazi iniziali e finali
SELECT Nome, TRIM(Nome) AS nome_senza_spazi FROM clienti;

-- 7. Sostituire una parte di testo
SELECT colore, REPLACE(colore, 'Rosso', 'Red') AS colore_modificato FROM prodotti;

-- 8. Cercare una sottostringa
SELECT Nome FROM clienti WHERE Nome LIKE 'A%';

-- 9. Inserire testo con zeri a sinistra
SELECT LPAD(codice_ordine, 5, '0') AS id_formattato, data_ordine FROM ordini;



-- Esercizi funzioni numeriche



-- 1. Arrotonda il prezzo dei prodotti a due decimali
SELECT nome_prodotto, prezzo, ROUND(prezzo, 2) AS prezzo_arrotondato
FROM prodotti;

-- 2. Calcola il valore assoluto della differenza tra quantità e 50
SELECT nome_prodotto, quantita, ABS(quantita - 50) AS differenza_assoluta
FROM prodotti;

-- 3. Calcola il quadrato della quantità dei prodotti
SELECT nome_prodotto, quantita, POWER(quantita, 2) AS quantita_al_quadrato
FROM prodotti;

-- 4. Trova la radice quadrata del prezzo di ogni prodotto
SELECT nome_prodotto, prezzo, SQRT(prezzo) AS radice_prezzo
FROM prodotti;

-- 5. Associa un numero casuale a ogni cliente
SELECT Nome, RAND() AS numero_casuale
FROM clienti;

-- 6. Mostra il prezzo massimo e minimo dei prodotti
SELECT MAX(prezzo) AS prezzo_massimo, MIN(prezzo) AS prezzo_minimo
FROM prodotti;

-- 7. Mostra il prezzo arrotondato per eccesso e per difetto
SELECT nome_prodotto, prezzo, CEIL(prezzo) AS arrotondato_eccesso, FLOOR(prezzo) AS arrotondato_difetto
FROM prodotti;

-- 8. Trova il resto della divisione tra quantità e 3 per ogni prodotto
SELECT nome_prodotto, quantita, MOD(quantita, 3) AS resto_divisione
FROM prodotti;

-- 9. Calcola la media dei prezzi dei prodotti
SELECT AVG(prezzo) AS prezzo_medio
FROM prodotti;



-- Funzioni data, ora, datetime



-- 1. Visualizza la data corrente per ogni ordine
SELECT codice_ordine, data_ordine, CURRENT_DATE AS data_corrente
FROM ordini;

-- 2. Calcola l'età in anni di ogni cliente in base alla data di registrazione
SELECT Nome, YEAR(CURRENT_DATE) - YEAR(data_registrazione) AS eta
FROM clienti;

-- 3. Estrai l'anno, il mese e il giorno dalla data di un ordine
SELECT codice_ordine, data_ordine, YEAR(data_ordine) AS anno, MONTH(data_ordine) AS mese, DAY(data_ordine) AS giorno
FROM ordini;

-- 4. Calcola il numero di giorni trascorsi tra la data dell'ordine e oggi
SELECT codice_ordine, data_ordine, DATEDIFF(CURRENT_DATE, data_ordine) AS giorni_trascorsi
FROM ordini;

-- 5. Aggiungi 10 giorni alla data di ogni ordine
SELECT codice_ordine, data_ordine, DATE_ADD(data_ordine, INTERVAL 10 DAY) AS data_modificata
FROM ordini;

-- 6. Sottrai 3 mesi alla data di ogni ordine
SELECT codice_ordine, data_ordine, DATE_SUB(data_ordine, INTERVAL 3 MONTH) AS data_modificata
FROM ordini;

-- 7. Mostra il giorno della settimana per ogni ordine (1 = Domenica, 7 = Sabato)
SELECT codice_ordine, data_ordine, DAYOFWEEK(data_ordine) AS giorno_settimana
FROM ordini;

-- 8. Formatta la data degli ordini nel formato "GG/MM/AAAA"
SELECT codice_ordine, data_ordine, DATE_FORMAT(data_ordine, '%d/%m/%Y') AS data_formattata
FROM ordini;

-- 9. Calcola il numero di mesi tra la data dell'ordine e oggi
SELECT codice_ordine, data_ordine, TIMESTAMPDIFF(MONTH, data_ordine, CURRENT_DATE) AS mesi_trascorsi
FROM ordini;