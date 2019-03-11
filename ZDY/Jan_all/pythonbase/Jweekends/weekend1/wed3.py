# # 打印出100行"I'm full"
# i = 1
# while i <= 100:
#     print("I'm full")
#     i+=50
# for x in range(1,101):
#     print("I'm full")
# # 使用while循环计算从1加到100的数字和.
# a = 1
# he = 0
# while a<=100:
#     a+=1
#     he+=a
# print(he)
# sum = 0
# for x in range(1,101):
#     sum += x
# print(sum)
# # 使用while循环计算100以内所有偶数的和
# b = 1
# sum = 0
# while b <= 100:
#     if b%2==0:
#         sum+=b
#     b+=1
# print(sum)
# sum = 0
# for x in range(0,100):
#     if x%2!=0:
#         continue
#     sum+=x
# print(sum)
# 每年存款 10 万, 年利率为:50%,
#   存够300万时,就退休 .
#   问多少年之后才能退休.
store = 10
total = 0
count = 0
while total <= 300:
    if store == 10 :
        total+=store    
    if count >= 0 :
        store = store + store*0.5
        total+=store
    count+=1
print(total)
print(count) 


