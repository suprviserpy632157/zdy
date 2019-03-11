select * from acct
where balance > 2000;

select * from acct
where acct_type <> 2;

select * from acct
where(acct_name = "Jerry" or
      acct_name = "Jim" or
      acct_name = "Jan")
    and status = 1
    and balance = 3000;

select * from acct 
where balance >= 3000 and balance <= 6000; 

select * from acct 
where acct_name not in("Jerry","Jim","Jan");

select acct_no,acct_name from acct 
where acct_name like '%t%';

select * from acct where acct_type is null;
select * from acct where acct_type is not null;

select acct_no,acct_name,balance
from acct order by acct_no;

select acct_no,acct_name,balance from acct limit 3;
select acct_no,acct_name,balance 
from acct order by balance desc 
limit 3;

select acct_no,acct_name,balance 
from acct order by balance desc 
limit 1,3;

create table page_demo(
    no varchar(8),
    name varchar(32)
);
insert into page_demo values
("1","Jerry"),("2","Tom"),
("3","Peter"),("4","Xinba"),
("5","Hanmeimei"),("6","Lilei"),
("7","Jim"),("8","Max"),
("9","Jan"),("10","Tim");
m = (页码-1)*每页显示的笔数
n = 每页笔数
select *from page_demo 
limit m,n;

select max(balance) from acct;

select status '状态',count(*) '数量',acct_type '类型'
from acct 
group by status,acct_type;

select max(balance),acct_type
from acct  
group by acct_type;

select acct_type,sum(balance)
from acct 
group by acct_type
having acct_type is not null;

insert into acct values
('6223456000007','Max','C0007',1,now(),1,9000.00),
('6223456000008','Hanmeimei','C0008',3,now(),1,5000.00),
('6223456000009','Lilei','C0009',2,now(),1,900.00),
('6223456000010','kxx','C0010',4,now(),1,9500.00),
('6223456000011','qyx','C0011',7,now(),1,2000.00),
('6223456000012','bdy','C0012',5,now(),1,1000.00);

select acct_type,sum(balance)
from acct
-- where acct_type in (1,2,3,4)
group by acct_type
having acct_type is not null
order by acct_type desc
limit 2; 

select acct_type,avg(balance)
from acct
where acct_type in (1,2,3,4,5,7)
group by acct_type 
having acct_type is not 1
order by acct_type
limit 10;