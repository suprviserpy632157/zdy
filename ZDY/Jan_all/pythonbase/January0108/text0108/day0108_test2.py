# 2.写一个函数get_chinese_char_count(s)，
#   此函数功能是给定一个字符串s，返回这个字符串中中文的个数
#   Def get_chinese_char_count(s)：
#   …
#   s=input（“请输入中英文混合的字符串”）
#   print（“中文的个数是：”，get_chinese_char_count(s)）
# 注：中文的编码范围是：0x4E00~0X9FA5
def get_chinese_char_count(s):
    count = 0
    for i in s:
        if 0x4E00<=ord(i)<=0x9FA5:
            count+=1
    return count
s = input("请输入中英文混合的字符串:")
print("中文的个数是：",get_chinese_char_count(s))