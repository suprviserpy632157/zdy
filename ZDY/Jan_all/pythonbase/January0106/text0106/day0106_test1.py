# 1.已知有一个字符串：
#   s =’100,200,300,500,800’
#   将其转化为列表，列表内都是整数，即：
#   L=[100,200,300,500,800] 
s ='100,200,300,500,800'
l=[int(i) for i in s.split(',')]
print(l)