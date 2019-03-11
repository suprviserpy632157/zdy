import time
class Phone:
    def __init__(self,name,price,CPU,screen_size):
        self.name = name
        self.price = price
        self.CPU = CPU
        self.screen_size = screen_size
    
    def startup(self):
        print("正在开机")
        time.sleep(2)
        print("开机成功")

    def shutdown(self):
        print("正在关机")
        time.sleep(2)
        print("关机成功")
    
    def call(self,phone_no):
        print("正在拨号")
        time.sleep(1)
        print("使用%s拨打和%s通话"%(self.name,phone_no))

    def send_msg(self,phone_no,msgss):
        print("使用%s发向%s发短信"%(self.name,phone_no))
        time.sleep(2)
        print("[%s]发送成功"%msgss)

    # 析构函数
    def __del__(self):
        print("__del__方法被调用")

def fun():
    phone=Phone("Iphone8",7999.99,"gt",5.5)
    print("fun()函数退出")

if __name__=="__main__":
    ph=Phone("Iphone8",7999.99,"gt",5.5)
    ph.startup()
    ph.shutdown()
    ph.call(13999999999)
    ph.send_msg(13999999999,"hello")
    # del ph  #会执行对象的析构函数
    fun()
    print("程序退出")
    # ph程序退出的时候被销毁