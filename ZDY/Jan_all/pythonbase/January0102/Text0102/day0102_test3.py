# 3.BMI指数（Body Mass Index）又称身体质量指数
#   BMI计算公式：BMI = 体重（公斤）/身高的平方（米）
#   如：
#     一个69公斤的人，身高是173公分
#     BMI = 69/1.73**2 得23.05
#   标准表：
#       BMI <18.5     体重过轻
#       18.5<=BMI< 24  正常体重
#       BMI>24        体重过重s
# 输入身高和体重，打印出BMI的值，并打印出体重情况
height = float(input("请输入您的身高："))
weight = float(input("请输入您的体重："))
BMI = weight/height**2
print(BMI)
if BMI <18.5:
    print("体重过轻")
elif 18.5 <= BMI <= 24:
    print("正常体重")
elif BMI > 24:
    print("体重过重")
else:
    pass

