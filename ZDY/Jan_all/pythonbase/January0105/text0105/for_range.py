i=6
for x in range(1,i): #range函数只执行了１次
    print('x=',x,'i=',i)
    i-=1
# 等同于
r= range(1,i)
for x in r:
    print('x=',x,'i=',i)
    i-=1