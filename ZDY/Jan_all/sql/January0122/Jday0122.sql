-- 1.创建数据库eshop，并制定为utf8编码
create database eshop
default charset = utf8;
-- 2.创建订单表（orders，utf8字符集），包含如下字段：
-- order_id    订单编号，字符串，32位
-- cust_id     客户编号，字符串，32位
-- order_date  下单时间，datetime类型
-- status      订单状态，枚举类型
-- 1-代付款，2-待发货，3-已发货，4-已收货，5-申请退款，6-已退货，9-废弃
-- products_num 包含的商品数量，整数型
-- amt         订单总金额，浮点，两位小数
create table orders(
    order_id varchar(32),
    cust_id varchar(32),
    order_date datetime,
    status enum("1","2","3","4","5","6","9"),
    products_num int(5) unsigned zerofill,
    amt decimal(10,2)
)default charset = utf8;
-- 3.在创建的orders表中至少插入5笔数据，数据看上去尽量真实
insert into orders values
("2103645548925246600","G007001","2019-01-30 11:20:54","1",200,20.00),
("2103645548925246601","G007002","2019-01-30 11:30:15","3",150,20.00),
("2103645548925246602","G007003","2019-01-30 16:18:47","4",300,20.00),
("2103645548925246603","G007004","2019-01-29 14:47:16","5",50,20.00),
("2103645548925246604","G007005","2019-01-28","2",350,20.00);
-- 4.编写SQL语句，实现如下功能：
--   1）	查找所有代付款的订单
select * from orders where status = "1";
--   2）	查找所有已发货，已收货，申请退货的订单
select * from orders where status in ("3","4","5");
-- where status = "3" or status = "4" or status = "5";
--   3）	查找某个客户待发货的订单
select * from orders where status = "2";
-- in ("2") ;
--   4）	根据订单编号，查找下单日期、订单状态
select order_date,status from orders where order_id ="2103645548925246602";
--   5）	查找某个客户所有订单，并按照下单时间倒序排列
insert into orders values
("2103645548925246605","G007004","2019-01-29 15:47:16","5",100,50.00),
("2103645548925246606","G007004","2019-01-29 11:47:16","5",600,10.00);
select * from orders where cust_id = "G007004"
order by order_date desc;
--   6）	统计每种状态订单的笔数
select status'状态',count(status)'笔数' from orders group by status;
--   7）	查找订单金额的最大值、最小值、平均值、总金额
select max(amt),min(amt),avg(amt),sum(amt) from orders;
--   8）	查询金额最大的前三笔订单
select * from orders order by amt desc limit 3;
--   9）	修改某个订单状态为”已收货”
update orders set status = "4" where order_id = "2103645548925246606";
--   10）	删除已废弃的订单
insert into orders values
("2103645548925246655","G007004","2019-01-29 15:48:16","9",100,50.00);
delete from orders where status = "9";


