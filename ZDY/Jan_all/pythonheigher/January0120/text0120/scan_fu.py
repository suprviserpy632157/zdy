# 编写一个程序，模拟扫福，各种福的概率如下：
# 爱国30%，敬业10%，和谐30%，友善20%，富强10%
# 编写代码进行模拟
# 0~99随机数
import random
f1,f2,f3,f4,f5 = 0,0,0,0,0
def gen_fu():
    global f1,f2,f3,f4,f5
    num = random.randint(0,99)  #产生100个随机数
    if num >= 0  and num <= 29 :      #爱国福
        f1 += 1
    elif num >= 30 and num <= 39 :    #敬业福
        f2 += 1
    elif num >= 40 and num <= 69 :    #和谐福
        f3 += 1
    elif num >= 70 and num <= 89 :    #友善福
        f4 += 1
    else:                             #富强福
        f5 += 1
for i in range(10000):
    # print("%d"%i)
    gen_fu()                           #产生福
total = f1+f2+f3+f4+f5
print("爱国福:%f"%(f1/total))
print("敬业福:%f"%(f2/total))
print("和谐福:%f"%(f3/total))
print("友善福:%f"%(f4/total))
print("富强福:%f"%(f5/total))
