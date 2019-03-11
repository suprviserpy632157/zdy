# 3.找一个文档完成如下操作
# 【1】	找到所有大写字母开头的单词
# 【2】	找到其中所有数字，数字包含整数，小数，分数，百分数，负数
#       （123  1.23  -1.5  -6  45%  1/2）
# 【3】	将所有日期格式2019-1-23变为2019.1.23
import re 
f = open('re.txt')
data = f.read()
# 大写字母开头单词(*后面可以加?,这样's就不会出来了)
pattern1 = r'\b[A-Z]\S*\b'
# 匹配数字
pattern2 = r'-?\d+\.?/?\d*%?'
# 日期格式替换
pattern3 = r'\d{4}-\d{1,2}-\d{1,2}'
regex1 = re.compile(pattern1)
for i in regex1.finditer(data):
    print(i.group())

regex2 = re.compile(pattern2)
for i in regex2.finditer(data):
    print(i.group())

regex3 = re.compile(pattern3)
for i in regex3.finditer(data):
    s = i.group()
    print(re.sub(r'-','.',s))

f.close()