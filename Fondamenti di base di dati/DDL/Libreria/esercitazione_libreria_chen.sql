-- 1. Elenco di tutti i libri
select * from libro;
-- 2. Elenco di tutti gli autori
select * from autore;
-- 3. Elenco di tutti gli editori
select * from editore;
-- 4. Selezionare il titolo e il prezzo dei libri ordinati per prezzo crescente
select titolo, prezzo
from libro
order by prezzo asc;
-- 5. Selezionare i libri con un prezzo superiore a 15€
select *
from libro 
where prezzo>15;
-- 6. Contare il numero totale di libri nel database
select count(*) as quantita_libri
from libro;
-- 7. Ottenere la media delle pagine dei libri
select avg(pagine)as media_pagine
from libro;
-- 8. Trovare il libro più costoso
select titolo,prezzo
from libro
where prezzo=(
select max(prezzo)
from libro
);
-- 9. Trovare il libro meno costoso
select titolo,prezzo
from libro
where prezzo=(
select min(prezzo)
from libro
);
-- 10. Contare il numero di autori per nazione
select nomecount(nome),nazionalita
from autore
group by nazionalita;
-- 11. Elenco dei libri con più di 500 pagine
select titolo,pagine
from libro
where pagine>500;
-- 12. Elenco degli autori italiani
select *
from autore
where nazionalita="IT";
-- 13. Trovare tutti i libri pubblicati da un determinato editore (es. Mondadori)
select * 
from libro, editore
where libro.editore_id = editore.id and editore.id=3;
-- 14. Contare il numero di libri per ogni editore
SELECT editore.nome AS editore, COUNT(libro.titolo) AS numero_libri
FROM libro
INNER JOIN editore ON libro.editore_id = editore.id
GROUP BY editore.nome
ORDER BY numero_libri DESC;
-- 15. Trovare i libri con più di 400 pagine pubblicati da un determinato editore
select titolo,editore.nome
from libro, editore
where libro.pagine>400 and editore.id=1;
-- 16. Trovare il numero di autori che hanno scritto almeno un libro
SELECT COUNT(DISTINCT autore_id) AS numero_autori 
FROM autore_libro;
-- 17. Trovare gli autori che hanno scritto più di un libro
SELECT autore.nome, autore.cognome, COUNT(autore_libro.libro_id) AS numero_libri
FROM autore
JOIN autore_libro ON autore.id = autore_libro.autore_id
GROUP BY autore.id
HAVING COUNT(autore_libro.libro_id) > 1;
-- 18. Trovare gli autori che non hanno scritto alcun libro
SELECT *
FROM autore
LEFT JOIN autore_libro ON autore.id = autore_libro.autore_id
WHERE autore_libro.libro_id IS NULL;
-- 19. Selezionare i libri con più di un autore
SELECT libro.titolo, COUNT(autore_libro.autore_id) AS numero_autori
FROM libro
JOIN autore_libro ON libro.id = autore_libro.libro_id
GROUP BY libro.id
HAVING COUNT(autore_libro.autore_id) > 1;

-- 20. Contare il numero di libri per autore
SELECT a.nome, a.cognome, COUNT(al.libro_id) AS numero_libri
FROM autore a
JOIN autore_libro al ON a.id = al.autore_id
GROUP BY a.id;
-- 21. Ottenere la somma totale del prezzo di tutti i libri
select sum(prezzo) as prezzo_totale
from libro;
-- 22. Contare il numero di libri con un prezzo compreso tra 10 e 20 euro
select count(titolo) as libri
from libro
where prezzo between 10 and 20;
-- 23. Trovare il prezzo medio dei libri per editore
select avg(prezzo),editore_id
from libro
group by editore_id;
-- 24. Trovare gli autori con più libri pubblicati da editori diversi
SELECT a.nome, a.cognome, COUNT(DISTINCT l.editore_id) AS numero_editori
FROM autore a
JOIN autore_libro al ON a.id = al.autore_id
JOIN libro l ON al.libro_id = l.id
GROUP BY a.id
HAVING COUNT(DISTINCT l.editore_id) > 1;
-- 25. Trovare i libri con il prezzo più alto per ogni editore
select max(prezzo),editore_id
from libro
group by editore_id;
-- 26. Ottenere i 5 libri più costosi
select prezzo
from libro
order by prezzo desc
limit 5;
-- 27. Contare il numero di libri pubblicati da ciascun editore con più di 3 libri
SELECT e.nome AS editore, COUNT(l.id) AS numero_libri
FROM libro l
JOIN editore e ON l.editore_id = e.id
GROUP BY e.nome
HAVING COUNT(l.id) > 3;
-- 28. Selezionare il nome degli editori che hanno pubblicato almeno un libro con più di 500 pagine
SELECT DISTINCT e.nome
FROM editore e
JOIN libro l ON e.id = l.editore_id
WHERE l.pagine > 500;
-- 29. Trovare gli autori che hanno scritto libri pubblicati da più di un editore
SELECT a.nome, a.cognome, COUNT(DISTINCT l.editore_id) AS numero_editori
FROM autore a
JOIN autore_libro al ON a.id = al.autore_id
JOIN libro l ON al.libro_id = l.id
GROUP BY a.id
HAVING COUNT(DISTINCT l.editore_id) > 1;
-- 30. Contare il numero di libri per ogni autore con più di 1 libro
SELECT a.nome, a.cognome, COUNT(al.libro_id) AS numero_libri
FROM autore a
JOIN autore_libro al ON a.id = al.autore_id
GROUP BY a.id
HAVING COUNT(al.libro_id) > 1;