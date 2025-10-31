DROP database IF EXISTS Portfolio;
create database Portfolio;
use Portfolio;
DROP TABLE IF EXISTS `Equipo`;

CREATE TABLE `usuario` (
  `Email` VARCHAR(40) not NULL,
  `Contraseña` VARCHAR(200) not NULL
);

CREATE TABLE `info` (
   id int auto_increment primary key,
  `tipo` VARCHAR(50),
  `tamano` BIGINT,
  `pixel` LONGBLOB,
  `sobre_mi` VARCHAR(400) not NULL,
  `tel` VARCHAR(400) not NULL,
  `mail` VARCHAR(400) not NULL,
  `dir` VARCHAR(400) not NULL,
  `edad` int not NULL
);
CREATE TABLE `Experiencia` (
  id int auto_increment primary key,
  exp VARCHAR(400) not NULL
);

CREATE TABLE `Proyectos` (
 id int auto_increment primary key,
  pro VARCHAR(400) not NULL
);

CREATE TABLE `EDUCACIÓN` (
id int auto_increment primary key,
  edu VARCHAR(400) not NULL
);

create TABLE `links` (
   id int auto_increment primary key,
  `name` VARCHAR(400) not NULL,
  `url` VARCHAR(400) not NULL
);

