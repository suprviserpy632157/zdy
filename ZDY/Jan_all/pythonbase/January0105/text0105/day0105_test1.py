# 1.输入一个整数，代表树干的高度，打印如下一颗圣诞树
# Eg：
# 请输入：2       输入：3
# 打印:           打印：
#     *                *
#    ***              ***
#     *              *****
#     *                *
#                      *
#                      *
height = int(input("Please input the number of tree's height:"))
for x in range(1,height*2,2):
    print(("*"*x).center(height*2-1))
else:
    for y in range(1,2*height,2):
        print("*".center(height*2-1)) 

# h = int(input("Please input the number of tree's height:"))       
# i=1
# j=1
# while i<h*2:
#     print(("*"*i).center(h*2-1))
#     i+=2
# else:
#     while j<2*h:
#         print("*".center(2*h-1))
#         j+=2

   
   
   
