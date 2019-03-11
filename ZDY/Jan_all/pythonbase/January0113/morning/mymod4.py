# mymod4.py
# 此实例示意模块的隐藏属性，当此模块用
# from import * 语句导入时，
# 不会导入_f,__f,和_name属性
def f():
    pass
def _f():
    pass
def __f():
    pass
name='aaa'
_name='bbb'