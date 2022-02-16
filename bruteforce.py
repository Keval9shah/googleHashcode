from itertools import combinations

x="""10
3 akuof byyii dlust
1 xdozp
3 dlust luncl qzfyo
1 xdozp
3 akuof luncl vxglq
1 qzfyo
3 dlust vxglq luncl
0
3 dlust xveqd tfeej
0
3 qzfyo vxglq luncl
1 byyii
3 luncl xdozp xveqd
1 sunhp
3 byyii xdozp tfeej
1 qzfyo
3 dlust akuof tfeej
1 xveqd
3 vxglq dlust byyii
1 akuof"""
m=x.split("\n")
no=int(m[0])
ingridientList=[] #contains both likes and dislikes from the initial text
for i in range(1,len(m)):
    ingridientList+=m[i].split(" ")[1:]
preferenceList=[] #contains both likes and dislikes from the initial text
for i in range(1,len(m)):
    preferenceList+=[m[i].split(" ")[1:]]
likeList=preferenceList[::2] #only the liked ingridients
dislikeList=preferenceList[1::2] #only disliked ingridients
del preferenceList
ingridientList=list(set(ingridientList))
# print(ingridientList)
comb=[]
for i in range(len(ingridientList)+1):
    comb+=combinations(ingridientList,i)
print(len(comb))
ctsList=[]
def check(i,j):
    for k in range(len(likeList[j])):
        if likeList[j][k] in i:
            pass
        else:
            return 0
    for k in range(len(dislikeList[j])):
        if dislikeList[j][k] not in i:
            pass
        else:
            return 0
    return 1
for i in comb:
    ans=0
    for j in range(no):
        ans+=check(i,j)
    ctsList+=[ans]
print(len(ctsList),max(ctsList))
indices = [i for i, x in enumerate(ctsList) if x == max(ctsList)]
for i in indices:
    print(comb[i])