from threading import Event
# 创建事件对象
e = Event()
# 设置e为非阻塞,wait就会变为非阻塞
e.set()
# 清除set状态,又变为阻塞状态
e.clear()
print(e.is_set())
e.wait(2)
print("******")