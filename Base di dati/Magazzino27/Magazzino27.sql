--create database Magazzino27;
create table Categoria(
Id int primary key,
Denominazione varchar(100),
Descrizione text null,
);
create table Prodotto(
Id int primary key not null,
Denominazione varchar(100) not null,
Descrizione text null,
Prezzo float not null,
Giacenza int not null,
IdCategoria int not null references Categoria(Id)
);
create table Cliente(
CodiceFiscale char(16) primary key not null,
Cognome varchar(50)not null,
Nome varchar(50)not null,
Telefono varchar(30) null,
Email varchar(50)not null unique,
);
create table IndirizzoSpedizione(
Id int primary key not null,
Indirizzo varchar(200),
Cap char(5)not null,
Citta varchar(100)not null,
Provincia char(2)not null,
IdCliente char(16) not null references Cliente(CodiceFiscale)
);
create table StatoOrdine(
Id int primary key not null,
Denominazione varchar(50)not null
);

create table Pagamento(
Id int primary key not null, 
Denominazione varchar(50),
Maggiorazione float not null
);

create table Ordine(
Riferimento char(8) primary key not null,
Data datetime not null,
IdCliente char(16) not null references Cliente(CodiceFiscale),
IdStatoOrdine int not null references StatoOrdine(Id),
IdIndirizzo int not null references IndirizzoSpedizione(Id),
IdPagamento int not null references Pagamento(Id)
);

create table DettaglioOrdine(
IdOrdine char(8),
IdProdotto int not null,
Quantita int not null,
primary key(IdOrdine,IdProdotto),
constraint FK_DettaglioOrdine_Ordine foreign key (IdOrdine) references Ordine(Riferimento),
constraint FK_DettaglioOrdine_Prodotto foreign key (IdProdotto) references Prodotto(Id)
);

--insert
insert into Categoria(id,Denominazione,Descrizione)
values(1,'Categoria 1',null);
insert into Categoria(id,Denominazione,Descrizione)
values(2,'Categoria 2',null);
insert into Categoria(id,Denominazione,Descrizione)
values(3,'Categoria 3','Descrizione categoria 3');

insert into Prodotto(Id,Denominazione,Descrizione,prezzo,Giacenza,IdCategoria)
values(1,'Prodotto 1',null,10.25,100,1);
insert into Prodotto(Id,Denominazione,Descrizione,prezzo,Giacenza,IdCategoria)
values(2,'Prodotto 2',null,10.25,100,2);
insert into Prodotto(Id,Denominazione,Descrizione,prezzo,Giacenza,IdCategoria)
values(3,'Prodotto 3',null,10.25,100,3);
insert into Prodotto(Id,Denominazione,Descrizione,prezzo,Giacenza,IdCategoria)
values(4,'Prodotto 4',null,10.25,100,1);
insert into Prodotto(Id,Denominazione,Descrizione,prezzo,Giacenza,IdCategoria)
values(5,'Prodotto 5',null,10.25,100,2);
--update
update Prodotto set Giacenza=0 where id=3;
update Prodotto set Giacenza=3 where id=4;
update Prodotto set Giacenza=30,prezzo=1.55 where id=2;
update Prodotto set Descrizione='Descrizione prodotto 1' where id=1
delete from prodotto where id=5;
select * from categoria;
select * from prodotto;
