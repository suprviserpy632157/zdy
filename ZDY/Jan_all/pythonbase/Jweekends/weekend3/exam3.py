# 用map、filter函数将列表中int类型
# 的元素转换成string类型并打印被修改的值
L=[1,2,3,'hello','world',6,7]
a=list(map(str,L))
print(a)
b=list(filter(str,a))
print(b)