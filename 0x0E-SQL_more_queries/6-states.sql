-- Creates the database hbtn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS `hbtn_0d_usa`;
CREATE TABLE IFNOT EXISTS `hbtn_0d_usa`.`states` (
    PRIMARY KEY(`id`),
    `id`   INT		NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(256) NOT NULL
);