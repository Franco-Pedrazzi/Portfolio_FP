DROP database IF EXISTS Portfolio;
create database Portfolio;
use Portfolio;
DROP TABLE IF EXISTS `Equipo`;

CREATE TABLE `usuario` (
  `Email` VARCHAR(40) not NULL,
  `Contraseña` VARCHAR(200) not NULL
);

CREATE TABLE `info` (
  `cv` VARCHAR(400) not NULL,
  `` VARCHAR(400) not NULL,
);

create TABLE `links` (
  `name` VARCHAR(400) not NULL,
  `url` VARCHAR(400) not NULL
);

