# 1.set.py
# 经理有３个人：曹操，刘备，孙权
# 技术员有：曹操，孙权，张飞，关羽
# 用集合求：
# 　　１．既是经理又是技术员的有谁？
# 　　２．是经理，但不是技术员的有谁？
# 　　３．是技术员，但不是经理的人有谁？
# 　　４．张飞是经理吗？
# 　　５．身兼一职的人都有谁？
# 　　６．经理和技术员共有几个？
manager={'曹操','刘备','孙权'}
technician ={'曹操','孙权','张飞','关羽'}
print('既是经理又是技术员的有:',manager&technician)
print('是经理，但不是技术员的有:',manager-technician)
print('是技术员，但不是经理的人有:',technician-manager)
if '张飞' not in manager:
    print("张飞不是经理")
else:
    print("张飞是经理")
print('身兼一职的人都有:',manager^technician)
print('经理和技术员共有',len(manager|technician),'个')