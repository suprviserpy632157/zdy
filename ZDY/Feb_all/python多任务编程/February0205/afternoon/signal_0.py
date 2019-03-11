# signal_0.py
# 理解:子进程退出发送信号,不会产生僵尸进程,
# 因为所有子进程结束后都会被处理,就算他们的父进程不处理,
# 系统也会帮助处理这些子进程
import signal
import os
# 处理子进程退出
signal.signal(signal.SIGCHLD,signal.SIG_IGN)

pid = os.fork()
if pid < 0:
    print("Error")
elif pid ==0:
    print("Child PID",os.getpid())
else:
    # 写死循环是威力让父进程不退出
    while 1:
        pass