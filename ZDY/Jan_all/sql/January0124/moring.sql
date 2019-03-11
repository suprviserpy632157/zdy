create table infos(
    id int not null primary key,
    name varchar(20),
    age int,
    score int
);

insert into infos(id) values(1),(2),(3);

create table infos2(
    id int,
    name varchar(20),
    course varchar(30),
    foreign key(id)
    references infos(id)
);

insert into infos2 values(1,"Jerry","MySQL"),(2,"Bob","PE");

update infos set score = 100 
where id=(select id from infos2 where course = "MySQL");

导出acct表中的数据
第一步：查看secure_file_priv变量值
show variables like "secure_file%"
第二步：执行导出
select * from acct
into outfile
'/var/lib/mysql-files/acct.csv'
fields terminated by ','
lines terminated by '\n';
第三步：查看导出结果（Linux命令行中执行）
sudo cat /var/lib/mysql-files/acct.csv

导入
load data infile 
'/var/lib/mysql-files/acct.csv'
into table acct
fields terminated by ','
lines terminated by '\n';

select * from acct
where cust_no in( -- 外层查询
  Select cust_no from customer
  where status = 1 -- 子查询
);

select * from acct 
where acct_no = ()

select * from (select * from xxxx)

select * from acct
where balance >
(select avg(balance) from acct); 

select * from acct where acct_no in 
(select acct_no from acct_trans_detail);

select * from acct where acct_no not in 
(select acct_no from acct_trans_detail);

select * from acct where acct_no not in  
(select acct_no from acct_trans_detail where amt > 1500);
-- 如果关联不正确，产生笛卡尔积
select a.acct_no,a.balance,b.amt
from acct a ,acct_trans_detail b
where a.acct_no = b.acct_no; -- 关联条件

select a.acct_no,a.acct_name,b.trans_date,b.amt
from acct a 
inner join acct_trans_detail b
on a.acct_no = b.acct_no;

练习：编写一个查询语句，从acct和customer表做内连接的查询，
查询结果包括的字典有acct_no acct_name cust_no tel_no
select a.acct_no,a.acct_name,c.cust_no,c.tel_no
from acct a 
inner join customer c 
on a.cust_no=c.cust_no;
或
select a.acct_no,a.acct_name,c.cust_no,c.tel_no
from acct a,customer c
where a.cust_no=c.cust_no;

select a.acct_no,a.acct_name,b.trans_date,b.amt
from acct a 
left join acct_trans_detail b
on a.acct_no = b.acct_no;

练习：编写一个查询语句，从acct和customer表做内连接的查询，
查询结果包括的字典有acct_no acct_name cust_no tel_no
select a.acct_no,a.acct_name,a.cust_no,c.tel_no
from acct_bak a 
left join customer c 
on a.cust_no=c.cust_no;

select a.acct_no,a.acct_name,b.trans_date,b.amt
from acct a 
right join acct_trans_detail b
on a.acct_no = b.acct_no;

grant select on *.* to 'Tom'@'localhost'
identified by '123456';
Flush PRIVILEGES; -- 刷新权限并生效 
-- 重新用Tom登录执行查询、验证插入
-- 查看user表中的权限，首先进入mysql库
select * from user where user ='Tom'\G

练习：对bank_user用户授权，能对bank库下所有表增删改查，限定能从
任意客户端登录，并将密码设为'123456'
grant insert,delete,update,select
on bank.* to 'bank_user'@'%'
identified by '123456';
Flush PRIVILEGES;

