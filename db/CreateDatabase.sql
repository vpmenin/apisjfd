USE Pycodebr;

CREATE TABLE carros(
    id integer not null auto_increment,
    marca varchar(100),
    modelo varchar(100),
    ano integer,
    PRIMARY KEY(id)
);

SET character_set_client = utf8;
SET character_set_connection = utf8;
SET character_set_results = utf8;
SET collation_connection = utf8_general_ci;

INSERT INTO carros(marca, modelo, ano) VALUES('FIAT','TIPO',1992);
INSERT INTO carros(marca, modelo, ano) VALUES('GM','ASTRA',2010);
INSERT INTO carros(marca, modelo, ano) VALUES('FORD','FIESTA',2020);
INSERT INTO carros(marca, modelo, ano) VALUES('VW','GOLF',2015);
INSERT INTO carros(marca, modelo, ano) VALUES('AUDI','A4',2015);



