# 2.写一个程序，以电子时钟格式打印时间：
#   格式为：
#      HH:MM:SS
def show_time():
    import time 
    while 1:
        t=time.localtime()
        #end="\r"\ｒ作用是将光标到第一个位置，这里起不断刷新的作用
        # print("%02d:%02d:%02d"%(t[3],t[4],t[5]),end="\r")
        print("%02d:%02d:%02d"%t[3:6],end="\r")
        #为了降低ＣＰＵ的占有率
        time.sleep(0.1)
show_time()

