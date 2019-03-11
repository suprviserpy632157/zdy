# 1.随机生成6位密码：
# 可以作为密码的字符
# 有a-z  A-Z  0-9
# def key_code():
#     import random
#     L=[]
#     for i in range(10):
#         L.append(i)
#     for i in range(65,91):
#         L.append(chr(i))
#     for i in range(97,123):
#         L.append(chr(i))
#     mykey=random.sample(L,6)
#     return mykey
# print(key_code())

# 密码中的字符可重复
import random
charator=[chr(x) for x in range(65,65+26)]
charator+=[chr(x) for x in range(97,97+26)]
charator+=[str(x) for x in range(10)]
passwd=''
for _ in range(6):
    passwd +=random.choice(charator)
print("密码是：",passwd) 
