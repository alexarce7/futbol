create database futbol;

use futbol;



create table equipos(
    
id_equipo int not null AUTO_INCREMENT PRIMARY KEY, 
    
nombre_eq varchar (50) not null,

partidosj int(3) not null,    
puntos int(3) not null,
    
tgoles int(3) not null,

golesf int(3) not null,
golesc int(3) not null);

create table usuarios(
nombre char(20) not null,
password varchar(20) null, primary key(nombre));

insert into usuarios (nombre, password) values ('arce', 'alejandro');