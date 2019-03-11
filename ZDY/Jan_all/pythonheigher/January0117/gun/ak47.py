# AK47类
from gun import *
class AK47(Gun):
    pass
    # def __init__(self):
    #     self.name="AK47"
    #     self.max_bullets=30 #弹夹最大容量
    #     self.bullet_left=0  #剩余子弹
    #     self.destructRatio=0.4 #杀伤系数
    
    # def reload(self): #填弹
    #     # 填单后剩余子弹数就等于弹夹容量
    #     self.bullet_left=self.max_bullets
    
    # def fire(self): #开火
    #     if self.bullet_left <= 0 : #没子弹了
    #         print("请填弹")
    #         return
    #     if self.bullet_left >= 3 :
    #         self.bullet_left -= 3 #打出３发子弹
    #     else: #子弹大于０小于３
    #         self.bullet_left = 0 #子弹全部打出去
    #     # 计算杀伤力
    #     damage = int(self.destructRatio*100)
    #     # 模拟声音
    #     print("哒哒哒，杀伤力%d,剩余子弹%d"%(damage,self.bullet_left))

        