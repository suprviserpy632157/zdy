# 通过函数的重写，实现自定义迭代器
class Myiter:
    # 用一个列表初始化对象
    def __init__(self,lst):
        self.data = lst    #lst是列表 
        self.cur_index = 0 #计数器
    
    def __iter__(self):    #返回可迭代对象
        return Myiter(self.data)
    
    def __next__(self):    #获取下一个元素
        if self.cur_index >= len(self.data):
            raise StopIteration   #抛出异常
        else:
            i = self.cur_index   #记录计数器
            self.cur_index += 1  #移动计数器
            return self.data[i]  #返回元素

if __name__ == "__main__":
    myiter = Myiter(range(1,10))
    for x in myiter:
        print(x,end=" ")
    print()        