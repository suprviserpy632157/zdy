# 输入多行文字，存入序列中，
# 每次输入后回车算一行，任意输入多行文字，
# 当直接输入回车结束（）
# 要求：
# １）按原输入内容在屏幕上输出
# ２）打印输入行数
# ３）打印一共输入的字符
# l=[]
# while 1:
#     x = input("Please input words:")
#     if not x :   #当用户直接输入回车时，得到空字符串
#         break
#     l.append(x) #将字符串x追加到l列表末尾
# print("l=",l)
# print("您输入的内容是：")
# for text in l:
#     print(text)
# print("您输入了",len(l),"行文字")
# count = 0
# for text in l:
#     count+=len(text) 
# print("您输入了",count,"个字符")

# shallow copy
# l1=[1,2,[3.1,3.2]]
# l2=l1.copy()
# l2[2][0]=3.14
# print(l1)
# print(l2)

# # deep copy
# import copy #导入拷贝模块
# l1=[1,2,[3.1,3.2]]
# l2=copy.deepcopy(l1)
# l2[2][0]=3.14
# print(l1)                     #[1,2,[3.1,3.2]]
# print(l2)
# 练习：有字符串＇ｈｅｌｌｏ＇生成字符串
# ＇ｈ ｅ ｌ ｌ ｏ＇和＇ｈ－ｅ－ｌ－ｌ－ｏ＇
# s='hello'
# s2 = ' '.join(s)
# print(s2)
# s3 ='-'.join(s)
# print(s3)
# 生成一个数值为1~9的整数的平方的列表，如：
# L=[1,4,3,16,25,36,49,64,81]
# 用循环语句：
# L = []
# for x in range(1,10):
#     L.append(x**2)
# L=[x**2 for x in range(1,10)]
# print("L=",L)
# 练习
# 用列表推导式生成１－１００以内所有奇数组成的列表
# L = [x for x in range(1,101) if x%2==1]
# # L = [x for x in range(1,100,2)]
# print("L=",L)
# 3.用字符串＇ＡＢＣ＇和＇１２３＇生成列表
# ['A1','A2','A3','B1','B2','B3','C1','C2','C3']
L = [x+y for x in 'ABC' for y in '123']
print(L)
# 生成一个列表，此列表为ｘ的平方加１不能被５整除的数的列表
# 条件：（ｘ＊＊２＋１）％５！＝０
# ｘ的取值范围是：０<= x < 100
l=[x for x in range(100) if (x**2+1)%5!=0]
print(l)