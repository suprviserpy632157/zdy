# class Student:
#     def __init__(self,name,phone_number,email):
#         self.name = name
#         self.phone_number = phone_number
#         self.email = email
    
#     def get_name(self):
#         return self.name
    
#     def get_phone(self):
#         return self.phone_number
    
#     def get_email(self):
#         return self.email
    
#     def __str__(self):
#         return "name=%s,phone=%s,email=%s"%(self.name,self.phone_number,self.email)

# if __name__ == "__main__":
#     s1 = Student("Bob","13888888888","666666@qq.com")
#     print(s1)

class Salary:

    total_money = 500000
    __slots__ = ["name","salary","month"]
    def __init__(self,name,salary,month):
        self.name,self.salary,self.month = name,salary,month
    @classmethod
    def total_salary(cls):
        print("总工资为:",cls.total_money)
a1 = Salary("wang",1000,3)
a1.__class__.total_money=1000000
print(a1.total_money)
Salary.total_salary()
print(a1.__class__)