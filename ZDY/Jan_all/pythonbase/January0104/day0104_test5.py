# # 打印九九乘法表
# i = 1
# while i <= 9 :
#     j = 1 
#     while j <= i :
#         print("%dx%d=%-2d"%(i,j,i*j),end=" ")
#         j+=1
#     print()   
#     i+=1

for x in range(1,10):
    for y in range(1,10):  
        if x<=y:
            print("%dx%d=%-2d"%(x,y,x*y),end=" ")
    print()