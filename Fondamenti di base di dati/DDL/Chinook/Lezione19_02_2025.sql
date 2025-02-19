create function somma(numero1 int,numero2 int)
returns int deterministic
return numero1+numero2;

select somma(4,3)as somma;
DELIMITER //

CREATE PROCEDURE GetPokemon(IN pokemon_id INT)
BEGIN
    INSERT INTO log(messaggio, utente) 
    VALUES (CONCAT('Richiesta informazione sul pokemon id ', pokemon_id));
    SELECT * 
    FROM pokemon 
    WHERE id = pokemon_id;
END //
DELIMITER ;

select * from ecommerce.log;

call ecommerce.GetPokemon(10);

drop procedure GetPokemon;

create table log(
id int primary key auto_increment,
messaggio varchar(50),
utente varchar(30)
);

alter table clienti
add column qta_ordini int;

delimiter &&
create trigger trig_aggiornaordini
after insert 
on Ordini for each row
begin
	update clienti set qta_ordini=qta_ordini+1 where cod_cliente= new.cod_cliente;
    end $$
delimiter ;