# 1.北京出租车计价程序
#   收费标准：
#     3公里以内收费13元
#     基本单价 2.3元/公里（超出3公里以外）
#     空驾费 ：超过15公里后，每公里加收单价的50%空驶费
#     （即：15公里后为3.45元/公里）
#   要求：
#     输入公里数，打印出费用金额
#    （以元为单位，精确到分，分以后四舍五入）
kilo = float(input("行驶距离是："))
if  kilo <= 3.0 :
    print("请支付１３元") 
elif 15 >=kilo > 3:
    pay_money1 = round((kilo-3)*2.3+13,2)
    print("请支付：",pay_money1,'元')
elif kilo > 15:
    pay_money2 = round((kilo-15)*3.45+(kilo-3)*2.3/n
    +13,2)
    print("请支付：",pay_money2,'元')
else:
    pass