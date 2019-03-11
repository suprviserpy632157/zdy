# 2.模拟斗地主发牌，牌共54张
# 种类：
# 黑桃（’\u2660’）,梅花（’\u2663’），
# 方块（’\u2665’），红桃（’\u2666’）
# 数字：
#   A2-10JQK
# 王牌：大小王
# 三个人，每人发17张牌，底牌留3张
# 输入回车，打印第一个人的17张牌
# 输入回车，打印第二个人的17张牌
# 输入回车，打印第三个人的17张牌
# 输入回车，打印三张底牌
import random as r
L=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
poke=['大王','小王']
kinds=['\u2660 ','\u2663 ','\u2665 ','\u2666 ']
player1=[]
player2=[]
player3=[]
for x in kinds:
    for y in L:
        s=x+y
        poke.append(s)
assert len(poke)==54,'出错'
poke+=[k+n for k in kinds for n in L]
poke2=poke.copy()
r.shuffle(poke2)
i=1
while i<=17:
    player1.append(poke2.pop())
    player2.append(poke2.pop())
    player3.append(poke2.pop())
    i+=1
print(player1)
input()
print(player2)
input()
print(player3)
input()
print(poke2)
# poke.extend(map(lambda x:"\u2660 "+ x,L))
# poke.extend(map(lambda x:"\u2663 "+ x,L))
# poke.extend(map(lambda x:"\u2665 "+ x,L))
# poke.extend(map(lambda x:"\u2666 "+ x,L))
# r.shuffle(poke)
# print(poke[0:17])
# input()
# print(poke[17:34])
# input()
# print(poke[34:51])
# input()
# print(poke[51:])


