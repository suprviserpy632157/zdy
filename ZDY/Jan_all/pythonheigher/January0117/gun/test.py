# 测试程序
import ak47
import awp

ak=ak47.AK47("AK47",30,0,0.4,3) #实例化AK47的对象
ak.reload()    #填弹
ak.fire()      #开火
print("---------------------------")
awp=awp.AWP("AWP",10,0,1.0,1) #实例化AWP对象
awp.reload()  #填弹
awp.openTelescope()
for i in range(0,10):
    awp.fire()    #开火
awp.fire()
awp.closeTelescope()

ak2 = ak47.AK47("AK47",20,0,0.4,3)