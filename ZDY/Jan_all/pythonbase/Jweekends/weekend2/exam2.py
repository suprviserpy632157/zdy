# ２．两个乒乓球队进行比赛，各出３人，甲队Ａ，Ｂ，Ｃ，
# 乙队X,Y,Z三人，以抽签决定比赛名单，Ａ说他不和Ｘ比，
# C说他不和Ｘ和Ｚ比，请编程序找出３对赛手的名单
for i in range(ord('X'),ord('Z')+1):
    for j in range(ord('X'),ord('Z')+1):
        if i!=j:
            for k in range(ord('X'),ord('Z')+1):
                if (i!=k)and(j!=k):
                    if (i!=ord('X')) and (k!=ord('X')) and (k!=ord('Z')):
                        print("A--%s\B--%s\C--%s"%(chr(i),chr(j),chr(k)))