# list1
# score=list()
# score.append(68)
# score.append(87)
# score.append(92)
# score.append(100)
# score.append(76)
# score.append(88)
# score.append(54)
# score.append(89)
# score.append(76)
# score.append(61)
# print(score[2])
# print(score[:6])
# score.insert(2,59)
# num=76
# print(score.count(num))
# if num in score:
#     print("1")
# else:
#     print("0")
# print(score.index(100))
# b=score.index(59)
# score[b]=60
# print(score)
# del(score[0])
# print(score)
# print(len(score))
# score.sort()
# print(score)
# score.reverse()
# print(score)
# score.pop()
# print(score)
# score.append(88)
# print(score)
# score.remove(88)
# print(score)
# score1=[80,61]
# score2=[71,95,82]
# print(score1+score2)
# score3=[80,61]
# score4=score3*5
# print(score4)

# list2
# a=['one','two','three']
# for i in a:
#     s=a[::-1]
# print(s)

a=[]
for i in range(10):
    a.append([])
    for j in range(10):
        a[i].append(0)
for i in range(10):
    a[i][0]=1
    a[i][i]=1
for i in range(2,10):
    for j in range(1,1+i):
        a[i][j]=a[i-1][j-1]+a[i-1][j]
for i in range(10):
    for j in range(1+i):
        print(a[i][j],sep＝'',end="")
    print("\n") 