name=['adam','LISA','barT']
def title():
    L=[]
    for i in name:
        print(list(map(i.title,name)))
# L=list(map(i.title for i in name ,name))
print(title())
