select a.FirstName,a.LastName,concat(b.FirstName, " ", b.LastName) as Responsabile 
from employee a
right join employee b on a.ReportsTo=b.EmployeeId;

-- Trova tutti gli album nella tabella Album.
select * 
from album;
-- Trova il nome degli artisti nella tabella Artist.
select * 
from artist;
-- Trova i dettagli dei clienti che vivono negli Stati Uniti.
select * 
from customer
where Country="USA";
-- Trova i dipendenti con il titolo "Sales Manager".
select * 
from employee
where title="Sales Manager";
-- Trova i generi musicali elencati nella tabella Genre.
select *
from genre;
-- Trova i dettagli degli album e degli artisti associati.
select *
from album
-- join artist on album.ArtistId=artist.ArtistId;
join artist using(artistid);
-- Trova i brani e i loro generi.
select track.Name, track.GenreId, genre.genreid, genre.Name
from track
join genre on track.GenreId=genre.GenreId;
-- Trova i dettagli delle fatture e dei clienti.
select *
from invoice
join customer using(customerid);
-- Trova le playlist e i brani associati.
select *
from playlisttrack as plt
join track using (trackid)
left join playlist using (playlistid);
-- Trova i brani con il rispettivo tipo di supporto.
select *
from track
left join mediatype using (mediatypeid);
-- Conta il numero totale di clienti.
select count(*)
from customer;
-- Calcola il totale delle vendite registrate nella tabella Invoice.
select sum(total)
from invoice;
-- Trova il prezzo massimo tra i brani nella tabella Track.
select max(unitprice)
from track;
-- Trova il numero di dipendenti per ogni città.
select city,count(*)
from employee
group by city;
-- Trova il prezzo medio per unità dei brani
select avg(unitprice)
from track;
-- Trova i brani più lunghi (durata superiore alla media).
select track.name,milliseconds
from track
where milliseconds > (
select avg(milliseconds) from track
);
-- Trova i dipendenti che non riportano a nessuno.
select *
from employee
where Reportsto is null;
-- Trova i clienti che non hanno effettuato fatture.
select *
from customer
where customerid not in (
							select customerid 
                            from invoice
);
-- Trova le città che hanno più di 2 dipendenti.
select  count(employeeid) as numemp, city 
from employee
group by city
having numemp>2;
-- Trova i brani appartenenti a generi diversi da "Rock".
select *
from track a
join genre b on a.genreid=b.genreid
where b.name!= "Rock";