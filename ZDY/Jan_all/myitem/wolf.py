# 狼人类
# 子类包括：普通狼人，白狼王
# 狼人：属性：
# 　　　能力：投票，夜晚杀一人（有分歧时，少数服从多数）
# 白狼王：投票，任何时候都能自爆带走一个人，夜晚杀人
# import time
# from all_player import *
# class Wolf(AllPlayer):
#     def __init__(self):
#         self.name = {0:"狼人",1:"狼人",2:"狼人",3:"白狼王"}
#         self.kno = self.no

#     def killone(self):
#         killno = int(input("请输入你们要杀的人:"))
#         for i in self.kno:
#             if killno == self.kno[i]:
#                 time.sleep(2)
#                 return killkno
#     def boom(self,i):
#         if self.name[3]:
#             return "自爆，带走%s"%self.no[i]
    
#     def __str__(self):
#         return self.name

# w1 = Wolf.killone([range(1,13)])

# insert into acct(acct_no,acct_name)
# values('622345000005','Emma');

# select acct_type,status from acct
# where acct_type = 2
# and status = 1;

A0 = dict(zip(('a','b','s','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i : i * i for i in A1}
A6 = [[i, i * i] for i in A1]
print(A0, A1, A2, A3, A4, A5, A6)

