import re

pattern = r"(\w+):(\d+)"
s = 'zhang:1994 li:1993'

l = re.findall(pattern,s)
print(l)

# 切割字符串
l = re.split(r'\s+','Hello world nihao     china')
print(l)

# 替换字符串匹配内容
s = re.sub(r'垃圾','**','张三垃圾,垃圾,垃圾',2)
print(s)

s = re.subn(r'垃圾','**','张三垃圾,垃圾,垃圾',2)
print(s)