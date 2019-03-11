# 3.用字典的方式完成下面一个小型的学生管理系统。
# 学生有下面几个属性：姓名，年龄，
# 考试分数包括：语文，数学，英语的分
print("--------------张明，李强的原始信息-------------------------")
ainfo={'name':'李明','age':'25','score':{'chinese':80,'math':75,'English':85}}
binfo={'name':'张强','age':'23','score':{'chinese':75,'math':82,'English':78}}
print(ainfo)
print(binfo)
print("---------------加一门Ｐｙｔｈｏｎ课-------------------------")
# 2.
ainfo['score']['python']=60
binfo['score']['python']=80
print(ainfo)
print(binfo)
print("---------------张强的数学成绩改为89-------------------------")
# 3.
binfo['score']['math']=89
print(binfo)
print("----------------删除李明的年龄------------------------")
# 4
ainfo.pop('age')
print(ainfo)
print("----------------排序张强的分数------------------------")
# 5
c=binfo['score'].values()
# c.sort()
print(c)
print("-----------------删除城市属性-----------------------")
# 6
binfo.pop("city",'beijing')
ainfo['city']='shanghai'
ainfo.pop("city",'beijing')
print(ainfo)
print(binfo)
