import re

# regex = re.compile(r'\w+',flags=re.A)
# regex = re.compile(r'[a-z]+',re.I)
# 匹配每一行开始位置
# regex = re.compile(r'^北京',flags=re.M)
pattern = r'''[A-Z][a-z]*  #匹配第一个单词
\s+\w+\s+  #匹配空行和第二个单词
\w+       #匹配汉字
'''
regex = re.compile(pattern,flags=re.X)
s = ''' Welcom to 
北京
'''
l = regex.findall(s)
print(l)