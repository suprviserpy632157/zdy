# 所有玩家类
from time import sleep
playerlist = [1,2,3,4,5,6,7,8,9,10,11,12]
class AllPlayer:
    def __init__(self,no = []):
        self.no = [x for x in no]

    def vote(self):
        count = 0  #记录玩家人数
        L=[]       #统计所有玩家投票
        L2=[]      #将得票数最多的玩家存入列表
        for i in self.no:
            num = int(input("%d号玩家，请选择你要投票的对象:"%playerlist[i-1]))
            sleep(0.1)
            count += 1     #记录玩家人数
            if num not in self.no or num == None:  #判断投票情况
                print("%d号家弃票"%playerlist[i-1])
            L.append(num)  #统计所有玩家投票
            for x in L:
                # 将票数过半的玩家存入L2
                if  (L.count(x) >= (len(L)//2)) and (x not in L2) :
                    L2.append(x)
                    print(L2)
        if count > (len(playerlist)//2):
            print("%s号玩家出局"%L2)
            del L2

a =AllPlayer(range(1,13))
a.vote()
print(playerlist)