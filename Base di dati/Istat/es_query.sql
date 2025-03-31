use istat
go

/* Selezione le ripartizioni geografiche d'Italia */
SELECT * 
FROM RipartizioneGeografica

/* Selezionare tutte le regioni d'Italia */
SELECT * 
FROM Regione

/* Selezionare le provincie d'Italia in ordine alfabetico crescente */
SELECT * 
FROM Provincia 
ORDER BY Denominazione ASC

/* Selezionare le regione del Nord-Ovest */
SELECT Regione.Denominazione AS 'Regione' 
FROM Regione 
INNER JOIN RipartizioneGeografica ON Regione.IdRipartizione=RipartizioneGeografica.Id
WHERE RipartizioneGeografica.Denominazione='Nord-Ovest'

/* NO! SELECT Denominazione FROM Regione WHERE IdRipartizione=1 */

/* Visualizzare la provincia e la sigla automobilistica 
delle provincie della regione Toscana */
SELECT Provincia.Denominazione AS 'Provincia', Provincia.Sigla AS 'Sigla Automobilistica'
FROM Provincia 
INNER JOIN Regione ON Provincia.IdRegione=Regione.Id
WHERE Regione.Denominazione='toscana'

/* Visualizzare il comune, il codice catastale, la provincia
di tutti i comuni appartenenti al Piemonte */
SELECT Comune.Denominazione AS 'Comune',
Comune.CodiceCatastale AS 'Codice catastale',
Provincia.Denominazione AS 'Provincia'
FROM Comune 
INNER JOIN Provincia ON Comune.IdProvincia=Provincia.Id
INNER JOIN Regione ON Provincia.IdRegione=Regione.Id
WHERE Regione.Denominazione='Piemonte'

/* Visualizzare la regione, la provincia, il comune 
che hanno altitudine dal centro minore di 500 metri */
SELECT Regione.Denominazione AS 'Regione',
Provincia.Denominazione AS 'Provincia',
Comune.Denominazione AS 'Comune',
Comune.AltitudineCentro
FROM Comune 
INNER JOIN Provincia ON Comune.IdProvincia=Provincia.Id
INNER JOIN Regione ON Provincia.IdRegione=Regione.Id 
WHERE Comune.AltitudineCentro<500

/* Visualizzare la popolazione al 2011 della provincia di Torino */
/* uso la funzione di aggregazione SUM */
SELECT SUM(Popolazione2011) as 'Popolazione al 2011' 
FROM Comune AS c 
INNER JOIN Provincia AS p ON c.IdProvincia=p.id
WHERE p.Denominazione='Torino'

/* Quanti sono i comuni del Nord-Est */
/* Funzione di aggregazione COUNT(*) */
SELECT COUNT(*) AS 'Totale dei comuni nel Nord-Est'
FROM Comune 
INNER JOIN Provincia ON Comune.IdProvincia=Provincia.Id
INNER JOIN Regione ON Provincia.IdRegione=Regione.Id
INNER JOIN RipartizioneGeografica ON Regione.IdRipartizione=RipartizioneGeografica.Id
WHERE RipartizioneGeografica.Denominazione='Nord-Est'

/* Quale comune ha il maggior numero di abitanti nel 2001 */
/* uso di TOP(n) con n = numero di record da visualizzare */
SELECT TOP(1) Comune.Denominazione as 'Comune', 
Popolazione2001 as 'Popolazione 2001'
FROM Comune
ORDER BY Comune.Popolazione2001 DESC

/* Visualizzare la popolazione nel 2011 minore d'Italia */
/* uso della funzione di aggregazione MIN */
SELECT MIN(Popolazione2011) as 'Popolazione minore'
FROM Comune

/* Visualizzare la superficie media dei comuni 
della provincia di Salerno */
/* uso funzione di aggregazione AVG(dominio) */
SELECT AVG(Superficie) as 'Superficie media'
FROM Comune c 
INNER JOIN  Provincia p ON c.IdProvincia=p.Id
WHERE p.Denominazione='Salerno'

/* Visualizzare la ripartizione geografica, la regione,
la provincia, il comune, la zona litoranea, l'altitudine dal centro, 
la superficie, la zona montana, la zona altimetrica 
di tutti i comuni capoluoghi */
/* uso degli alias obbligatorio */
SELECT rg.Denominazione AS 'Ripartizione Geoagrafica'
, r.Denominazione AS 'Regione'
, p.Denominazione AS 'Provincia'
, c.Denominazione AS 'Comune'
, c.AltitudineCentro, c.Superficie,c.ZonaLitoranea
, za.Denominazione AS 'Zona Altimetrica'
, 'Comune ' + zm.Denominazione AS 'Zona Montana'
FROM RipartizioneGeografica AS rg 
INNER JOIN Regione r ON rg.id=r.IdRipartizione
INNER JOIN Provincia p ON p.IdRegione=r.Id
INNER JOIN Comune c ON c.IdProvincia=p.Id
INNER JOIN ZonaAltimetrica za ON za.Id=c.IdZonaAltimetrica
INNER JOIN ZonaMontana zm ON zm.Id=c.IdZonaMontana
WHERE c.ComuneCapoluogo=1