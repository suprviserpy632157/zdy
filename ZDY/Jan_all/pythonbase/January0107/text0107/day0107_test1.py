# 1.	思考下面的程序执行结果是什么？为什么？
# L=list(range(10))
# For x in L:
# L.remove(x)
# Print(‘L=’,L)   #请问是空列表码？ 
l=list(range(10))
for x in l:
    l.remove(x)
print("l=",l)
# 不是空列表，因为删[0],[1]会前移，以此类推
# 是由列表的性质决定的