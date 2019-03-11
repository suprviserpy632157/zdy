class A:
    def __init__(self,name):
        self.name=name 
    
    # def __str__(self): #重写__str__函数
    #     return "name = %s"%self.name

class B(A):
    def __init__(self,name,id):
        super().__init__(name)  #调用父类构造方法
        self.id=id
    
    def __repr__(self): #重写__repr__方法
        return "B('%s','%s')"%(self.name,self.id)

    # def __str__(self): #重写__str__函数
    #     return "name = %s,id = %s"%(self.name,self.id)

b=B("Jerry","0001")  #==)
print(b)
# print(b)  #Ｂ中重写__str__方法，所以可以直接打印
# str_obj = repr(b) 
# print(str_obj)
# new_obj = eval(str_obj) #通过python的解释器（对用eval函数）还原对象
# print(new_obj)
# super(B,b).print() #根据对象ｂ找到父类，并调用父类的print方法


