# # 1.写一个程序，输入三行文字，让这三行文字依次以２０个字符的
# # 宽度右对齐输出
# line1 = input("请输入第一行文字：")
# line2 = input("请输入第二行文字：")
# line3 = input("请输入第三行文字：")
# # print('%20s'%line1)
# # print('%20s'%line2)
# # print('%20s'%line3)
# # 思考：能否以最长的字符串长度进行右对齐显示（左侧填充空格）
# max_len=len(line1)
# if len(line2)>max_len:
#     max_len=len(line2)
# if len(line3)>max_len:
#     max_len=len(line3)
# print('Max:',max_len)
# # max_len = max(len(line1),len(line2),len(line3))
# # print(' '*(max_len-len(line1))+line1)
# # print(' '*(max_len-len(line2))+line2)
# # print(' '*(max_len-len(line3))+line3)
# fmt='%'+str(max_len)+'s'
# print(fmt%line1)
# print(fmt%line2)
# print(fmt%line3)

# while语句嵌套
# 写程序打印１～２０的整数，打印在１行内并将结果打印１０行
# j=1
# while j<=10:
#     i = 1
#     while i<=20:
#         print(i,end=' ')
#         i += 1
#     print()
#     j+=1
# 输入一个数，打印指定宽度的正方形
# w = int(input("please input a number:"))
# i = 1
# while i <= w :
#     count = 1
#     while count <= w:
#         print(count,end=' ')
#         count+=1
#     print()
#     i+=1
# 练习：用ｗｈｉｌｅ语句实现打印三角形，输入一个整数
# 表示三角形的宽度和高度，打印出相应的三角形
# １）＊　　　　　　　　２）　　　　＊
# 　　＊＊　　　　　　　　　　　　＊＊
# 　　＊＊＊　　　　　　　　　　＊＊＊
# 　　＊＊＊＊　　　　　　　　＊＊＊＊
# ３）＊＊＊＊　　　　　４）＊＊＊＊
# 　　　＊＊＊　　　　　　　＊＊＊
# 　　　　＊＊　　　　　　　＊＊
# 　　　　　＊　　　　　　　＊
num = int(input("please input a height:"))
stars = 1 #*的个数和行数
while stars <= num :
    print(stars*"*")
    stars+=1
star1=1
while star1<=num: 
    blank = num - star1  # 计算出左侧空格的个数
    print(' '*blank+"*"*star1)
    star1+=1
st = num  #代表星号个数
while st > 0 :
    blank1=num-st
    print(' ' * blank1+ '*'*st)
    st -= 1 #每一行＊号少一个
s = num 
while s > 0:
    blank2 = num - s
    print("*"*s)
    s-=1

    
