create table myexcel(
    name varchar(20),
    phnumber int,
    height int,
    liking varchar(25)
);

insert into myexcel values
("Jerry",90,80,"singing"),
("Jim",90,90,"climbing"),
("Jane",90,100,"swimming"),
("Tom",90,110,"writing");

create table student(
    stu_no varchar(32),
    stu_name varchar(128)
);

alter table student add age int;-- 添加到最后
alter table student add id int first;-- 添加到最前面
alter table student 
add tel_no varchar(32) 
after stu_name;-- 添加到指定字段后

-- 修改学生名称长度为64
alter table student modify stu_name varchar(64)
-- 修改age字段名称为stu_age
alter table student change age stu_age int;
-- 删除id字段
alter table student drop id;

create table customer(
    cust_no varchar(32) not null,
    cust_name varchar(128) not null,
    tel_no varchar(32) not null
)default charset=utf8;

-- 插入一笔带空值的数据
insert into customer(cust_no,cust_name)
values('c0001','Jerry');

create table customer(
    cust_no varchar(32) unique,
    cust_name varchar(128) not null,
    tel_no varchar(32) not null
)default charset=utf8;
insert into customer
values('c0001','Jerry','13999998888');
insert into customer
values('c0001','Jerry','15948762302');

create table customer(
    cust_no varchar(32) primary key,
    cust_name varchar(128) not null,
    tel_no varchar(32) not null
)default charset=utf8;
-- 插入cust_no重复或为空的均报错  
insert into customer
values('c0001','Jerry','13999998888');
insert into customer
values('c0001','Jerry','15948762302');
insert into customer
values(null,'Jerry','1999995444');

create table customer(
    cust_no varchar(32) default '001',
    cust_name varchar(128) not null,
    tel_no varchar(32) not null
)default charset=utf8;
alter table customer add status int default 0;
insert into customer(cust_no,cust_name,tel_no)
values('c0001','Jerry','13999998888');
insert into customer
values('c0001','Jerry','15948762302');
insert into customer
values(null,'Jerry','1999995444')

create table ai_test(
    id int primary key auto_increment,
    name varchar(32)
);
insert into ai_test values(null,'Tom');