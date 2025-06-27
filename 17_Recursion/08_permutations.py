que = [1,2,3]
ans = []
temp=[]

def permutations(que, temp=[]):
    if len(temp) == len(que):
        ans.append(temp[:])
        return
        
    for i in range(len(que)):
        if que[i] in temp:
            continue
        temp.append(que[i])
        permutations(que, temp)
        temp.pop()
        
permutations(que, temp)
print(ans)