-- 外键示例
create table account( 
    acct_no varchar(32) primary key,
    cust_no varchar(32) not null,
    -- 添加外键约束
    constraint fk_cust_no 
    foreign key(cust_no)
    references customer(cust_no)
)default charset=utf8;
-- 在account中插入cust_no为"C0001"的数据
-- 插入失败，插入失败（account参照了一个不存在的实体）
insert into account values
("622345000001",'C0001');
-- 往customer中插入数据
insert into customer(cust_no,cust_name,tel_no)
values('C0001',"Jerry",'13999999999');

insert into account values
("622345000001",'C0001');

delete from customer where cust_no = "C0001";

create table acct_trans_detail(
    trans_sn varchar(32) not null, -- 交易流水号
    trans_date datetime not null, -- 交易时间
    acct_no varchar(32) not null, -- 账号
    trans_type int null, -- 交易类型
    amt decimal(10,2) not null, -- 交易金额
    unique(trans_sn),-- 交易流水键唯一索引
    index(trans_date) -- 交易日期普通索引
);
insert into acct_trans_detail values
('201801010001',now(),'622345000001',1,1000);

-- 在acct_trans_detail表acct_no字段上
-- 创建普通索引
-- acct_trans_detail为表明；idx_acct_no为索引名称；acct_no为字段名称
alter table acct_trans_detail
add index idx_acct_no(acct_no);
或
create index idx_acct_no on 
acct_trans_detail(acct_no);

create table acct_new
select * from acct;

create table acct_new
select * from acct where balance < 2000;

create table acct_new
select * from acct where 1 = 0;

alter table acct rename to acct_new;


作业：
１．修改表orders,在order_id上添加主键
alter table orders change order_id order_id varchar(32) primary key;
或
alter table orders modify order_id varchar(32) primary key;
２．在cust_id,order_date,products_num字段添加非空约束
alter table orders change cust_id cust_id varchar(32) not null;
alter table orders change order_date order_date datetime not null;
alter table orders change products_num products_num int not null;
３．在status字段上添加默认值，默认为１
alter table orders change status 
status enum("1","2","3","4","5","6","9") 
default '1';
４．在order_date字段上添加普通索引
alter table orders add index(order_date);
或
create index idx_order_date on orders(order_date);
或
alter table orders add index idx_acct_no(acct_no);