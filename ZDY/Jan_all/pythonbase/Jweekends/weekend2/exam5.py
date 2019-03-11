# 5.１元钱一瓶汽水，喝完后两个空瓶换一瓶汽水，
# 问：你有２０元，最多可以喝到几瓶汽水？
def gas_water(money):
    n=1
    s=0
    sum =money
    while n!=0:
        n=money//2
        s=money%2
        money=n+s
        sum = sum +n
    return sum
a=gas_water(20)
print(a)