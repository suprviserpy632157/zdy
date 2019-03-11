# 15!=15*14*13*12*11*10*9...*1
i = 1 
j = 1
while i<=15:
    j*=i
    i+=1
print(j)
# 找到100以内所有素数(质数)
a=2
while a<100:
    if a%2 !=0 :
        print(a,end=" ")
    a+=1
print()
    
        