create database if not exists negozio;
-- 1
CREATE TABLE IF NOT EXISTS prodotti (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    nome VARCHAR(50) NOT NULL,
    prezzo DECIMAL(6,2) NOT NULL,
    quantita INT NOT NULL
);
-- 2
alter table prodotti
add descrizione varchar(300) after nome;
-- 3
CREATE TABLE IF NOT EXISTS ordini (
    id INT AUTO_INCREMENT PRIMARY KEY, 
    data date NOT NULL,
    totale DECIMAL(10,2) NOT NULL,
    id_cliente INT NOT NULL
);
-- 4
CREATE TABLE IF NOT EXISTS clienti (
    id INT AUTO_INCREMENT PRIMARY KEY,  
    nome VARCHAR(30) NOT NULL,          
    cognome VARCHAR(30) NOT NULL,       
    email VARCHAR(100) NOT NULL,        
    provincia VARCHAR(2) NOT NULL          
);
-- 5
alter table clienti	
modify column cognome varchar(30);
alter table clienti
add telefono varchar(20) after cognome;
-- 6
CREATE TABLE IF NOT EXISTS americhe (
    id INT AUTO_INCREMENT PRIMARY KEY,  
    stato VARCHAR(50) NOT NULL,         
    capitale VARCHAR(50) NOT NULL       
);
CREATE TABLE IF NOT EXISTS europa (
    id INT AUTO_INCREMENT PRIMARY KEY,  
    stato VARCHAR(50) NOT NULL,         
    capitale VARCHAR(50) NOT NULL       
);
CREATE TABLE IF NOT EXISTS africa (
    id INT AUTO_INCREMENT PRIMARY KEY,  
    stato VARCHAR(50) NOT NULL,         
    capitale VARCHAR(50) NOT NULL       
);
-- 7
CREATE TABLE IF NOT EXISTS libro (
    id INT AUTO_INCREMENT PRIMARY KEY,   
    titolo VARCHAR(100) NOT NULL,         
    prezzo DECIMAL(6,2) NOT NULL,         
    pagine INT NOT NULL,                  
    id_editore INT NOT NULL               
);
-- 8
RENAME TABLE clienti TO customers;
