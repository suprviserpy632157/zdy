# create table num_test(
#   -- 显示３位无符号整数，左边０填充
#   card_type int(3) unsigned zerofill,
#   dis_rate decimal(10,2)
# );
# insert into num_test values(1,0.88);
# insert into num_test values(100,23.456);
# insert into num_test values(01000,23.444);
# insert into num_test values(2,2);

# create table enum_test(
#   name varchar(32),
#   sex enum('boy','girl'),
#   course set('music','dance','paint')
# );
# insert into enum_test values
# ("Jerry",'girl','music,dance');
# insert into enum_test values
# ("Jerry",'girl','music,dance,football');

# update acct
#     set status = 3,
#         balance = balance - 100
#   where acct_no = '622345000001';

# delete from acct where acct_no = '622345000005';
'hello world'.split(" ")