# 2.写程序，用while语句生成如下字符串，并打印出来
#   1) ‘ABCD…XYZ’
#   2) ‘AaBbCcDd……XxYyZz’
# i = 65
# while i < 65+26 :
#     print(chr(i),end='')
#     i+=1
# print()
# j = 65
# while  j <= 90:
#     print("%s"%chr(j)+"%s"%chr(j+32),end ="")
#     j+=1
# print()
# 方法二
s = ''   #此字符串用来累加大写字符
code = 65   #ｃｏｄｅ＝　ｏｒｄ（＇Ａ＇）
while code <ord('A')+26:
    ch = chr(code)  #用当前编码转为字母
    s+=ch  #把生成的字母加到ｓ中
    code+=1
print("s=",s)

s2 = ''   #此字符串用来累加大小写字符
code = 65   #ｃｏｄｅ＝　ｏｒｄ（＇Ａ＇）
while code <ord('A')+26:
    ch = chr(code)  #用当前编码转为大写字母
    s2+=ch  #把生成的字母加到ｓ中
    ch = chr(code+32)
    s2+=ch
    code+=1
print("s2=",s2)
