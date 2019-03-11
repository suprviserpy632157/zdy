import re

pattern = r"\d+"
s = "2019年4月28日"

it = re.finditer(pattern,s)
# print(dir(next(it)))

for i in it:
    print(i.group()) #取出match对象匹配内容

# 完全匹配
try:
    obj =  re.fullmatch(r'\w+','hello_1973')
    print(obj.group())
except AttributeError:
    pass

# 匹配开始
obj = re.match(r'[A-Z]\w+','Hello World')
print(obj.group())

# 匹配第一个
obj = re.search(r'\d+','2019年12月24日')
print(obj.group())