# 3.输入3行文字，让这3行文字在一个方框居中显示
#   （注：不要输入中文）
# eg：输入
# hello！
# I’m studying python！
# I like python！
# 打印如下：
#   +----------------------+
#   |       hello！        |
#   |I’m studying python！ |
#   |    I like python！   |
#   +----------------------+
line1 = input("请输入第一行文字：")
line2 = input("请输入第二行文字：")
line3 = input("请输入第三行文字：")
max_len = max(len(line1),len(line2),len(line3))
print("+-"+"-"*max_len+"-+")
print("| "+line1.center(max_len,)+" |")
print("| "+line2.center(max_len,)+" |")
print("| "+line3.center(max_len,)+" |")
print("+-"+"-"*max_len+"-+")
# lenth =int(input("请输入方框的宽度:"))
# line1 = input("+"+"-"*(lenth-2)+"+")
# s ="hello!"
# line2 = input("|"+s.center(lenth-2,) +"|")
# s1 = "I’m studying python！"
# line3 = input("|"+s1.center(lenth,)+"|")
# s2 = "I like python！"
# line4 = input("|"+s2.center(lenth-2,)+"|")
# line5 = input("+"+"-"*(lenth-2)+"+")
# max_len = max(len(line2),len(line3),len(line4))
# if lenth>=max_len:
#     print(line1)
#     print(line2)
#     print(line3)
#     print(line4)
#     print(line5)
# else:
#     pass
    