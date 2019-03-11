# 枪械类
class Gun:
    def __init__(self,name,max_bullets,bullet_left,dest_Ratio,firing_bullets):
        self.name = name
        self.max_bullets = max_bullets      #弹夹最大容量
        self.bullet_left = bullet_left      #剩余子弹数量
        self.destructRatio = dest_Ratio     #杀伤系数
        self.firing_bullets=firing_bullets  #每次开火击发子弹数量
    
    def reload(self): #填弹
        # 填单后剩余子弹数就等于弹夹容量
        self.bullet_left=self.max_bullets
        print("填弹完成，剩余子弹%d发"%self.bullet_left)
    
    def fire(self): #开火
        if self.bullet_left <= 0 : #没子弹了
            print("请填弹")
            return
        if self.bullet_left >= self.firing_bullets :
            self.bullet_left -= self.firing_bullets #打出一次击发打出的子弹
        else: #子弹大于０小于一次击发打出的子弹
            self.bullet_left = 0 #子弹全部打出去
        # 计算杀伤力
        damage = int(self.destructRatio*100)
        # 打印，模拟开火
        print("%s开火,杀伤力%d,剩余子弹%d"%(self.name,damage,self.bullet_left))
