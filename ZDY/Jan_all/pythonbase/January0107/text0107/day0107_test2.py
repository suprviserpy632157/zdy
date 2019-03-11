# 2.输入一些单词和解释，将单词作为键，解释作为值，
# 存入字典中，当输入单词或解释为空时，
# 停止输入，并打印这个字典
# 然后，输入查询的单词，给出单词的内容，
# 如果单词不存在，则提示查无此词
#创建一个空字典准备存储数据
d={}
while 1:
    words=input("please input word:")
    if not words: #如果words绑定空字符串，则退出
        break
    means=input("please input word:"+words+" means:")
    if not means:  #如果means绑定空字符串，则退出
        break
        # 走到此处，说明words和means都绑定了正确的值
    d[words]=means
print("d=",d)
print("begin research...")
while 1:
    w=input("please input research word:")
    if w in d:
        print("the word mean:",d[w])
    else:
        print("查无此词")
    if w not in d:
        break
    
