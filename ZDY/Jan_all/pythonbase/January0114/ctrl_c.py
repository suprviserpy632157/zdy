try:
    import time
except ImportError:
    print("asd")

try:
    while 1:
        time.sleep(1)
        print(time.asctime())
except KeyboardInterrupt:
    pass
