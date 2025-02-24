drop database if exists ecommerce;
create database ecommerce;
use ecommerce;
CREATE TABLE prodotti (
    codice_prodotto VARCHAR(10) PRIMARY KEY,       -- Codice prodotto
    nome_prodotto VARCHAR(100) NOT NULL,        -- Nome del prodotto
    colore VARCHAR(50),                 -- colore del prodotto
    taglia VARCHAR(10),                 -- taglia del prodotto
    magazzino VARCHAR(10)               -- Codice magazzino
);

CREATE TABLE fornitori (
    codice_fornitore VARCHAR(10) PRIMARY KEY,       -- Codice fornitore
    nome_fornitore VARCHAR(100) NOT NULL,        -- Nome del fornitore
    numero_soci INT,                          -- Numero di soci
    sede VARCHAR(100)                   -- Sede del fornitore
);

CREATE TABLE clienti (
    codice_cliente VARCHAR(10) PRIMARY KEY, -- Codice cliente
    Nome VARCHAR(100) NOT NULL,         -- Nome del cliente
    Email VARCHAR(100),                 -- Email del cliente
    data_registrazione DATE DEFAULT (CURRENT_DATE) -- Data di registrazione
);
CREATE TABLE prodotti_archivio (
    codice_prodotto VARCHAR(10) PRIMARY KEY,       -- Codice prodotto
    nome_prodotto VARCHAR(100) NOT NULL,        -- Nome del prodotto
    colore VARCHAR(50),                 -- colore del prodotto
    taglia VARCHAR(10)                  -- taglia del prodotto
);

CREATE TABLE ordini (
    codice_ordine VARCHAR(10) PRIMARY KEY,  -- Codice ordine
    codice_cliente VARCHAR(10) NOT NULL,    -- Codice cliente
    data_ordine DATE NOT NULL,           -- Data dell'ordine
    FOREIGN KEY (codice_cliente) REFERENCES clienti(codice_cliente)
);

CREATE TABLE vendite (
    codice_vendita VARCHAR(10) PRIMARY KEY, -- Codice vendita
    codice_prodotto VARCHAR(10) NOT NULL,  -- Codice prodotto
    Quantita INT NOT NULL,             -- Quantità venduta
    PrezzoUnitario DECIMAL(10, 2),     -- Prezzo per unità
    Totale DECIMAL(10, 2),             -- Totale della vendita
    FOREIGN KEY (codice_prodotto) REFERENCES prodotti(codice_prodotto)
);

CREATE TABLE fornitori_prodotti (
    codice_fornitore VARCHAR(10) NOT NULL,          -- Codice fornitore
    codice_prodotto VARCHAR(10) NOT NULL,          -- Codice prodotto
    Qta INT NOT NULL,                   -- Quantità fornita
    PRIMARY KEY (codice_fornitore, codice_prodotto),           -- Chiave primaria composita
    FOREIGN KEY (codice_fornitore) REFERENCES fornitori(codice_fornitore),
    FOREIGN KEY (codice_prodotto) REFERENCES prodotti(codice_prodotto)
);

CREATE TABLE ordini_temp (
    codice_ordine VARCHAR(10) PRIMARY KEY,  -- Codice ordine temporaneo
    codice_cliente VARCHAR(10) NOT NULL,    -- Codice cliente
    data_ordine DATE NOT NULL            -- Data dell'ordine
);
