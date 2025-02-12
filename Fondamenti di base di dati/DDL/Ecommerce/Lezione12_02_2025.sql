insert into prodotti
values
("P011","Cravatta","gialla","Unica","MZ01")
;
update prodotti
set colore = "rosso"
where codice_prodotto="P001";

delete from prodotti
where magazzino="MZ003";

insert into fornitori
values
("F01","Giggino","212","TO"),
("F02","Pino","213","MI"),
("F03","Pina","214","MI")
;
select *
from fornitori;
update fornitori
set numero_soci=numero_soci+2
;
delete from fornitori_prodotti
where codice_prodotto="P004";
-- 9. Recuperare i dettagli delle vendite per prodotti il cui prezzo unitario è maggiore della media
select *
from vendite
where PrezzoUnitario>(select avg(PrezzoUnitario)
						from vendite);
-- 5. Recuperare i dettagli dei fornitori che forniscono almeno un prodotto di colore "verde"                        
select *
from fornitori f
join fornitori_prodotti fp on f.codice_fornitore=fp.codice_fornitore
join prodotti p on fp.codice_prodotto=p.codice_prodotto
where colore="Verde";

select c.nome
from clienti c
join ordini o on c.codice_cliente = o.codice_cliente;

select nome,email, data_registrazione
from clienti
where data_registrazione>=current_date - interval 410 day;
-- where datediff(current_date,data_registrazione)<=30;
update fornitori
set sede="Napoli"
where codice_fornitore="F002";

delete from fornitori
where sede="Napoli";

update prodotti
set taglia="L"
where colore="Verde";

delete from fornitori 
where numero_soci<5;

-- 10. Trovare i prodotti venduti esclusivamente nel magazzino "MZ001"
select magazzino,v.codice_prodotto,p.codice_prodotto
from prodotti p
join vendite v on v.codice_prodotto=p.codice_prodotto
where magazzino="MZ01";
-- 9. Inserire dati nella tabella di associazione
insert into fornitori_prodotti
values
("F001","P002",100)
;
select * 
from fornitori_prodotti;