import re

pattern = r"(ab)cd(?P<pig>ef)"

regex = re.compile(pattern)

# 获取match对象
obj = regex.search('abcdefgh')
######### match 属性变量 ##########
print(obj.pos)
print(obj.endpos)
print(obj.re)
print(obj.string)
print(obj.lastgroup)
print(obj.lastindex)
print("++++++++++++++++++++++++++++++++++++++++++")
########## match 属性方法 ##########
print(obj.span())
print(obj.start())
print(obj.end())

print(obj.groupdict())
print(obj.groups())

print(obj.group())
print(obj.group(1))
print(obj.group('pig'))