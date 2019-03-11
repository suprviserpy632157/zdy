# 3.写一个myrange()函数，参数可以传1~3个，
# 实际意义同range（）函数规则相同，返回符合
# range（…）函数规则的列表
# eg：
# L= myrange(4)
# print（L） #[0,1,2,3]
# L= myrange(4,6)
# print(L)  #[4,5] 
# L= myrange(1,10,3)
# print(L)  #[1,4,7]
# def myrange(*args):
#     L=[]
#     if len(args)==1:
#         start,end,step=0,args[0],1
#         while start<args[0]:
#             L.append(start)      
#             start+=1
#         print(L,end=" ")
#         print()
#         return ""
#     elif len(args)==2:
#         start,end,step=args[0],args[1],1
#         while start<args[1]:
#             L.append(start)           
#             start+=1
#         print(L,end=" ")
#         print()
#         return ""
#     elif len(args)==3:
#         start,end,step=args[0],args[1],args[2]
#         while start<args[1]:
#             if start%args[2]==1:
#                 L.append(start)
#             start+=1
#         print(L,end=" ")
#         print()
#         return ""
#     else:
#         pass
# L=myrange(4)
# print(L)
# L= myrange(4,6)
# print(L)
# L= myrange(1,10,3)
# print(L)

def myrange(start,stop=None,step=None):
    if stop is None:   
        stop=start
        start=0
    if step is None:
        step=1
    #开始，结束，步长都已确定
    # return [x for x in range(start,stop,steps)]
    if step >0:
        L=[]
        while start <stop:
            L.append(start)
            start+=step
        return L
    elif step<0:
        L=[]
        while start>stop:
            L.append(start)
            start+=step
        return L
L=myrange(4)
print(L)
L= myrange(4,6)
print(L)
L= myrange(1,10,3)
print(L)
L=myrange(10,0,-2)
print(L)
