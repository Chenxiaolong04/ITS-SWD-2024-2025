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
-- 8. Trovare il libro più costoso--------------------------------------------------------------------------------------
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

-- 15. Trovare i libri con più di 400 pagine pubblicati da un determinato editore
select titolo,editore.nome
from libro, editore
where libro.pagine>400 and editore.id=1;
-- 16. Trovare il numero di autori che hanno scritto almeno un libro

-- 17. Trovare gli autori che hanno scritto più di un libro

-- 18. Trovare gli autori che non hanno scritto alcun libro

-- 19. Selezionare i libri con più di un autore

-- 20. Contare il numero di libri per autore
select count(nome)
from autore
group by nome;
-- 21. Ottenere la somma totale del prezzo di tutti i libri
select sum(prezzo) as prezzo_totale
from libro;
-- 22. Contare il numero di libri con un prezzo compreso tra 10 e 20 euro
select count(titolo) as libri
from libro
where prezzo between 10 and 20;
-- 23. Trovare il prezzo medio dei libri per editore

-- 24. Trovare gli autori con più libri pubblicati da editori diversi

-- 25. Trovare i libri con il prezzo più alto per ogni editore

-- 26. Ottenere i 5 libri più costosi
select prezzo
from libro
order by prezzo desc
limit 5;
-- 27. Contare il numero di libri pubblicati da ciascun editore con più di 3 libri

-- 28. Selezionare il nome degli editori che hanno pubblicato almeno un libro con più di 500 pagine

-- 29. Trovare gli autori che hanno scritto libri pubblicati da più di un editore

-- 30. Contare il numero di libri per ogni autore con più di 1 libro