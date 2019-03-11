# 1.一个球从100米高空落下，每次落地后反弹高度
# 为原高度的一半，再落下，写程序算出：
# 1）皮球在第10次落地后反弹的高度
# 2）皮球在第10次落地反弹后共经历多少米路程
# height=100
# meter=height/2
# for i in range(0,10):
#     height=(2*meter)+height
#     meter=meter/2
# print(height)
# print(meter)
def get_last_height(height,times):
    """height　原来的高度
    　　times  为反弹的次数"""
    for _ in range(times):
        height /=2  #每次反弹的高度为原高度的一半
    return height
print("皮球从100米的高度落下反弹10次后高度为：",get_last_height(100,10))   
def get_discentance(height,times):
    meter = 0
    for _ in range(times):
        # 累加下落过程的路程
        meter+=height
        height/=2  #计算反弹后的高度
        # 累加反弹后的路程
        meter+=height
    return meter
print("皮球从100米的高度落下反弹10次后的总路程为：",get_discentance(100,10))