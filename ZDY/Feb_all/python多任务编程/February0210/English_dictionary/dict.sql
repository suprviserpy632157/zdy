create database dict default charset = utf8;
-- 用户信息表
create table user(
    id int primary key auto_increment,
    name varchar(32) not null,
    passward varchar(16) default "00000000"
);
-- 历史信息表
create table hist(
    id int primary key auto_increment,
    name varchar(32) not null,
    word varchar(32) not null,
    time varchar(64)
);
-- 单词表
create table words(
    id int primary key auto_increment,
    word varchar(32) ,
    interpret text
);