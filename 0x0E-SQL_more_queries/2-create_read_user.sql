-- To create database hbtn_0d_2 and user user_0d_2
-- user_0d_2 has SELECT privileges on htbn_0d_2with password
CREATE DATABASE
    IF NOT EXISTS `htbn_0d_2`;
CREATE USER
    IF NOT EXISTS 'user_0d_2'@'localhost'
    IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT
   ON `hbtn_0d_2`.*
   TO 'user_0d_2'@'localhost';
