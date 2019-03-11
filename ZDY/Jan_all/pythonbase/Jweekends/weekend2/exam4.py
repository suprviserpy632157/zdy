# 4.要求用户输入总资产，例如2000
# 显示商品列表，让用户根据序号选择商品，加入购物车
# 购买，如果商品总额大于总资产，提示用户余额不足，
# 否则，购买成功
goods=[
      {"name":"电脑","price":"1999"},
      {"name":"鼠标","price":"10"},
      {"name":"游艇","price":"20"},
      {"name":"美女","price":"998"},
      ]
def Status(price1,status1,sumall):
    if status1 == 1:
        sumall = AddPrice(price1,sumall)
        return sumall
    if status1 == 0:
        sumall = MinusPrice(price1,sumall)
        return sumall 

def AddPrice(price1,a,sumall):
    sumall=sumall+price1
    return sumall 

def MinusPrice(price1,sumall):
    sumall = sumall-price1
    return sumall

money1=int(input("请输入您的总资产："))
sumall=0
status1=1
while 1:
    while 2:
        for n in range(len(goods)):
            print("商品序号"+str(n+1)+":"+goods[n]['name']+str(goods[n]['price'])+"元")
        a=int(input("请输入您想购买的商品序号")-1)
        sumall = Status(goods[a]['price'].status1,sumall)
        if sumall>money1:
            status1=0
            sumall=Status(goods[a]['price'].status1,sumall)
            print("您的资产不够，请重新输入")
            continue
        else:
            break

