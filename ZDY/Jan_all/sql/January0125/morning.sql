grant insert,delete,update,select
on *.* to 'zdy'@'%'
identified by '123456'
with grant option;
Flush PRIVILEGES;

start transaction;
update acct set balance = balance -100 
  where acct_no = '622345000001';
update acct set balance = balance + 100
  where acct_no = '622345000001';
commit; -- 或rollback
-- 在提交事物前，重新登录一个客户端，
-- 查看数据是否变更 

create table t1(
    id int primary key
)engine=InnoDB default charset=utf8;

alter table t1 engine = InnoDB;