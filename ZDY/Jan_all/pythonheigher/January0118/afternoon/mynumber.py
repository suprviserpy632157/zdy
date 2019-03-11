# mynumber.py
# 自定义数字类型
# 数值转换函数重写示例
class Mynumber:
    def __init__(self,value):
        self.data = value  #值，字符串类型

    def __int__(self):
        return int(float(self.data))
    
    def __float__(self):
        return float(self.data)
    
    def __complex__(self):
        return complex(self.data)

if __name__=="__main__":
    num=Mynumber("123.45")
    print(hasattr(num,"data"))
    print(hasattr(num,"aaaa"))
    delattr(num,"data")
    print(hasattr(num,"data"))
    # setattr(num,"data","456.78")
    # print(getattr(num,"data"))
    # print(num.data)
    # print(int(num))
    # print(float(num))
    # print(complex(num))
    