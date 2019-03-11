# 用map、filter函数筛选，匹配出所有含有
# ｈｅｉｇｈｔ这个键的字典并将对应的值打印出来
people=[{'name':'Mary','height':160},{'name':'LsLa','height':80},{'name':'Sam'}]
def find_h():
    value=0
    for i in people:
        value=i.get('height')
    return value
print(find_h())