# 3.写一个闹钟程序，启动时设置
# 定时时间，到时间后打印一句
# “时间到”然后程序退出
# import time
# def alarm(h,m):
#     while 1:
#         cur_time=time.localtime()
#         print("%02d:%02d:%02d"%cur_time[3:6],end='\r')
#         time.sleep(1)
#         if(h,m)==cur_time[3:5]:
#             print("时间到")
#             return
# if __name__=='__main__':
#     hour=int(input("请输入定时的小时："))
#     minute=int(input("请输入定时的分钟："))
#     alarm(hour,minute)

def alarm(hour,minute):
    import time
    while 1:
        #拿到当前时间
        t=time.localtime()
        print("%02d:%02d:%02d"%t[3:6],end='\r')
        time.sleep(0.1)
        # if t[3]==hour and t[4]==minute:
        if t[3:5]==(hour,minute):
            print("时间到!!!")
            return
h=int(input("请输入定时的小时："))
m=int(input("请输入定时的分钟："))
alarm(h,m)
