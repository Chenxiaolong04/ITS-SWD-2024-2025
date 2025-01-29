-- 1. Selezionare tutti i paesi e i loro dati
select *
from `country-data`;
-- 2. Selezionare solo il nome dei paesi
select country
from `country-data`
order by country
limit 5,10; -- salta i primi 5 e prende i 10 successivi
-- 3. Selezionare i paesi con un'aspettativa di vita superiore a 70 anni
select country, life_expec
from `country-data`
where life_expec>70;
-- 4. Selezionare i paesi con un PIL pro capite maggiore di 10.000
select country as Paese, gdpp as PIL
from `country-data`
where gdpp >10000
order by gdpp desc;
-- 5. Trovare i paesi con un tasso di mortalità infantile inferiore a 20

-- 6. Ordinare i paesi per reddito pro capite in ordine decrescente

-- 7. Ordinare i paesi per aspettativa di vita in ordine crescente

-- 8. Selezionare i paesi con un tasso di fertilità superiore a 5

-- 9. Trovare i paesi con una spesa sanitaria superiore al 10% del PIL
select country, health
from `country-data`
where health > 10;
-- 10. Selezionare i paesi con un'inflazione negativa (deflazione)

-- 11. Trovare i paesi con esportazioni che superano il 50% del PIL
select country, exports
from `country-data`
where exports > 50;
-- 12. Trovare i paesi con importazioni maggiori delle esportazioni

-- 13. Selezionare i paesi con un PIL pro capite compreso tra 5.000 e 10.000

-- 14. Trovare i paesi con un tasso di fertilità inferiore a 2 e un'aspettativa di vita superiore a 75 anni
SELECT country, total_fer, life_expec
FROM `country-data`
WHERE 
    total_fer > (
        SELECT AVG(total_fer)
        FROM `country-data`
        WHERE life_expec > 70
    );

-- 15. Selezionare i paesi con un tasso di mortalità infantile maggiore di 100

-- 16. Trovare i paesi con reddito pro capite maggiore di 15.000 e inflazione inferiore a 5%

-- 17. Ordinare i paesi per spesa sanitaria in ordine decrescente
select country, health
from `country-data`
order by health desc;
-- 18. Selezionare i paesi con un PIL pro capite inferiore a 2.000

-- 19. Trovare i paesi con esportazioni e importazioni combinate superiori al 90% del PIL
select country, (exports + imports) as total
from `country-data`
where (exports + imports) > 90;
-- 20. Trovare i 3 paesi con il più alto rapporto tra spesa sanitaria e reddito pro capite
select country, (health/gdpp) as rapporto
from `country-data`
order by rapporto desc
limit 3;
-- 21. Trovare il rapporto tra fertilità totale e aspettativa di vita per ogni paese e ordinarlo in ordine crescente
select country, (total_fer/life_expec)as rapporto
from `country-data`
order by rapporto asc;
-- 22. Calcolare la media del tasso di fertilità per i paesi con un’aspettativa di vita superiore a 70 anni
select country, total_fer
from `country-data`
where life_expec > 70;
-- 23. Trovare i paesi con il massimo e il minimo reddito pro capite
SELECT country, (income) as RPP
FROM `country-data`
WHERE
income = (SELECT MIN(income) FROM `country-data`)
OR
income = (SELECT MAX(income) FROM `country-data`);
-- 24. Contare il numero di paesi con inflazione negativa
select count(country)
from  `country-data`
where inflation<0;
-- 25. Trovare i 5 paesi con il PIL pro capite (gdpp) più alto

-- 26. Calcolare la somma delle esportazioni e delle importazioni per ciascun paese

-- 27. Trovare i paesi dove il totale delle esportazioni è almeno il doppio delle importazioni
select country, exports,imports
from `country-data`
where exports>=imports*2;
-- 28. Calcolare il PIL pro capite medio (gdpp) per ogni gruppo di aspettativa di vita (fasce di 10 anni)
select floor(life_expec/10)*10 as range_eta,avg(gdpp) as media_PIL
from  `country-data`
group by range_eta 
order by range_eta;
-- 29. Trovare i paesi con un tasso di mortalità infantile superiore alla media globale

-- 30. Trovare i paesi con il massimo tasso di mortalità infantile in ogni fascia di reddito