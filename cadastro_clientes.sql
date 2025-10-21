-- criando o banco de dados
create database techsolutions DEFAULT character set utf8mb4;

-- criando um usuario para o app
create user 'cadastro_app '@'localhost' IDENTIFIED BY 'amanda123';


-- dar permissao ao banco

grant all privileges on techsolutions.* to 'cadastro_app'@'localhost';
flush privileges;

-- usar o banco 

use techsolutions;

-- criando a  tabela de clientes 

create table if not exists clientes(
id int auto_increment primary key,
nome varchar(60) not null,
cpf varchar(14) not null unique,
email varchar(100) not null,
telefone varchar (15),
endereco varchar(200),
estado CHAR(2)
);


select * from clientes;

