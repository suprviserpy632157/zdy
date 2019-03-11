# 输入3行文字，将这三行文字保存于一个列表中，并打印
# eg：
# 请输入:ABC       
# 请输入:123
# 请输入:你好
# 生成如下打印列表并打印：
# Print（L） #[‘ABC’,’123’,’你好’] 
L=[]
line1 = input("Please input the first line word:")
line2 = input("Please input the first line word:")
line3 = input("Please input the first line word:")
L+=line1,line2,line3
# L=[line1,line2,line3]
print(L)