# 狙击枪类
from gun import *
class AWP(Gun):
    def __init__(self,tele_type):
        self.tele_type = tele_type

    def openTelescope(self): #打开瞄准镜
        print("瞄准镜已打开")
    
    def closeTelescope(self): #关闭瞄准镜
        print("瞄准镜已关闭")   
    # def __init__(self):
    #     self.name="awp"
    #     self.max_bullets=10 #弹夹最大容量
    #     self.bullet_left=0  #剩余子弹
    #     self.destructRatio=1.0 #杀伤系数
    
    # def reload(self): #填弹
    #     # 填单后剩余子弹数就等于弹夹容量
    #     self.bullet_left=self.max_bullets
    
    # def fire(self): #开火
    #     if self.bullet_left <= 0 : #没子弹了
    #         print("请填弹")
    #         return
    #     # 计算剩余子弹
    #     self.bullet_left -= 1 #打出1发子弹
    #     # 计算杀伤力
    #     damage = int(self.destructRatio*100)
    #     # 模拟声音
    #     print("嘣，杀伤力%d,剩余子弹%d"%(damage,self.bullet_left))

        