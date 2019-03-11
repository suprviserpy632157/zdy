def perm_k(list,stack):
    if not list:
        print(stack)
    else:
        for i in range(len(list)):
            stack.append(list[i])
            del list[i]
            perm_k(list,stack)
            list.insert(i,stack.pop())
list=[1,2,3]
stack=[]
perm_k(list,stack)
#     if len(arrs)==1:
#         return [arrs]
#     if k==1:
#         return list(map(lambda s:[s],arrs))
#     result=[]
#     for i in range(len(arrs)):
#         rest_arrs=arrs[:i]+arrs[i+1:]
#         rest_list=perm_k(rest_arrs,k-1)
#         lists=[]
#         for term in rest_list:
#             lists.append(arrs[i:i+1]+term)
#         result+=lists
#     return result
# print(perm_k([1,2,3],1))
