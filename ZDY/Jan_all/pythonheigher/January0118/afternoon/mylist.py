# 自定义列表
class Mylist:
    def __init__(self,iterable = []):
        self.data = [x for x in iterable]
    # 重写__abs__()函数
    def __abs__(self):
        # 将每个元素求绝对值，用产生的结果实例化一个Mylist对象
        return Mylist(abs(x) for x in self.data)
    
    def __len__(self):
        return len(self.data)
        # count=0
        # for x in self.data:
        #     count+=1
        # return count
    
    def __round__(self):
        return Mylist(round(x,2) for x in self.data)

    def __reversed__(self):
        temp=[]
        x=len(self.data)-1  #最后一个元素下标
        while x >=0:
            temp.append(self.data[x])
            x -= 1  #计数器减1
        return Mylist(temp)  #temp是经过倒序的可迭代对象
        # return Mylist(reversed(self.data))

    def __add__(self,rhs):     #一个对象加另一个对象
        return Mylist(self.data+rhs.data)

    def __mul__(self,rhs):     #L1*2     
        return Mylist(self.data*rhs)

    def __str__(self):
        return "data:%s"%self.data

    # def __str__(self):  #重写__str__()函数
    #     ret = ""
    #     for x in self.data:
    #         ret += str(x) #将元素由数字转换成字符串
    #         ret += "," 
    #     return ret #返回结果串

    def __eq__(self,value):  #  重载==运算符
        len1=len(self.data)  #  获取data属性长度
        len2=len(value)      #　获取另一个对象data的长度
        if len1!=len2:
            return False
        for i in range(len1): 
            if self.data[i]!=value.data[i]:
                return False
            else:
                continue
        return True

    def __ne__(self,value):   # 在重载==的基础上重载!=
        return not(self == value)

    def __gt__(self,value):   #  >
        len1=len(self.data)       #  获取data属性长度
        len2=len(value)           #  获取另一个对象data的长度
        min_len = min(len1,len2)  #  获取循环上限

        for i in range(min_len):
            if self.data[i] == value.data[i]:
                continue
            elif self.data[i] > value.data[i]:
                return True
            elif self.data[i] < value.data[i]:
                return False
        if len1 == len2:     #相等
            return False
        elif len1 > len2:    #前面的元素相等，长度比对方大
            return True
        else:
            return False

    def __lt__(self,value):  # <
        len1=len(self.data)       #  获取data属性长度
        len2=len(value)           #  获取另一个对象data的长度
        min_len = min(len1,len2)  #  获取循环上限

        for i in range(min_len):
            if self.data[i] == value.data[i]:
                continue
            if self.data[i] < value.data[i]:
                return True
            if self.data[i] > value.data[i]:
                return False
        if len1 == len2:
            return False
        elif len1 < len2:
            return True
        else:
            return False

    def __neg__(self):  #重载－运算符
        return Mylist(-x for x in self.data)

    def __contains__(self,e): #重载in/not in运算符重载
        print("__contains__()被调用")
        return e in self.data

    def __getitem__(self,i):  #重载索引的__getitem__()运算符
        return self.data[i]
    
    def __setitem__(self,i,value):  #重载索引的__setitem__()运算符
        self.data[i]=value    #设置的时候不需要返回值

    def __delitem__(self,i):  #重载索引的__delitem__()运算符
        del self.data[i]
        
if __name__=="__main__":
    L=Mylist([-1,+2,-3,+4,-5])
    print(L[0])
    L[2]=333
    print(L)
    del L[2]
    print(L)
    # print(-L)  #对对象执行负号运算
    # print(2 in L)
    # print(4 not in L)
    # L=Mylist([1,2,4,8])
    # L2=Mylist([1,2,4])
    # print(L>L2)
    # print(L<L2)
    # L3=L1+L2
    # print(L3)
    # L4=L1*2
    # print(L4)
    # L=Mylist([-1,2,-3,5.6789])
    # L2 = abs(L)  #重写了__abs__()函数，支持abs表达式
    # print(L2)  #重写__str__()函数,所以支持print()
    # L3 = len(L)
    # print(L3)
    # L4 = round(L)
    # print(L4)
    # L5 = reversed(L)
    # print(L5)
    # # 打印自定义列表中所有元素的绝对值
    # for x in L.data:
    #     print(abs(x))
    # print()
    # # 将所有的元素近似值打印
    # for x in L.data:
    #     print(round(x,2))