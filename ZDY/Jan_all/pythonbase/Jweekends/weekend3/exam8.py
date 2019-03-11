import os
a=[]
def zuozhan(dirpwd):
    if not os.path.exists(dirpwd):
        return dirpwd.'is not found!'
    for i in os.listdir(dirpwd):
        a.append(os.path.splitext(dirpwd+i)[-1])
    print list(set(a))
zuozhan()