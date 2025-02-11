create database ecommerce;

create table prodotti(
	codp varchar(10) primary key,
    nome varchar(100) not null,
    color varchar(50),
    taglia varchar(10),
    magazzino varchar(10)
);
create table fornitori(
	codf varchar(10) primary key,
    nome varchar(100) not null,
    nSoci int,
    sede varchar(100)
);
create table clienti(
	cod_cliente varchar(10) primary key,
	nome varchar(100) not null,
    email varchar(100),
    data_registrazione date default (current_date)
);
create table prodottiArchivio(
	codp varchar(10) primary key,
	nome varchar(100) not null,
    color varchar(50),
    taglia varchar(10)
);
create table ordini(
	codOrdine varchar(10) primary key,
    cod_cliente varchar(10) not null,
    data_ordine date not null,
    foreign key(cod_cliente) references clienti(cod_cliente)
);

create table vendite(
	codVendita varchar(10) primary key,
    codprodotto varchar(10) not null,
    quantita int not null,
    prezzo_unitario decimal (10,2),
    total decimal(10,2),
    foreign key (codprodotto) references prodotti(codp)
);
create table FornitoriProdotti(
	codf varchar(10) not null,
	codp varchar(10) not null,
    qta int not null,
    primary key(codf,codp), -- chiave primaria composta
	foreign key(codp) references prodotti(codp),
	foreign key(codf) references fornitori(codf)
);
create table OrdiniTemp(
	codOrdine varchar(10),
    cod_cliente varchar(10) not null,
    data_ordine date not null
);
