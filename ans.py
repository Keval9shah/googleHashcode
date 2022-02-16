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
preferenceList=[] #contains both likes and dislikes from the initial text
for i in range(1,len(m)):
    preferenceList+=[m[i].split(" ")[1:]]
likeList=preferenceList[::2] #only the liked ingridients
dislikeList=preferenceList[1::2] #only disliked ingridients
del m
del preferenceList
ingridientDictionary={} #ranks the ingridients based on likes and dislikes(+1 for like and -1 for dislike)
for i in range(no):
    for j in range(len(likeList[i])):
        try:
            ingridientDictionary[likeList[i][j]]+=1#/len(likeList[i])
        except:
            ingridientDictionary[likeList[i][j]]=1#/len(likeList[i])
    for j in range(len(dislikeList[i])):
        try:
            ingridientDictionary[dislikeList[i][j]]-=1#*len(dislikeList[i])
        except:
            ingridientDictionary[dislikeList[i][j]]=-1#*len(dislikeList[i])
customerList=[0 for i in range(no)] #ranks the customers based on their preferences
for y in range(no):
    t=0
    for z in range(len(likeList[y])):
        t+=ingridientDictionary[likeList[y][z]]
    for z in range(len(dislikeList[y])):
        t-=ingridientDictionary[dislikeList[y][z]]
    customerList[y]=t
customerDict={i:customerList[i] for i in range(no)} #converts list into dict
compareList=sorted(customerDict.items(), key = lambda kv:(kv[1], kv[0]),reverse=True) #sorts the dict
print(ingridientDictionary)#----------
print(customerList)#------------
del customerList
del customerDict
inlist=[]
outlist=[]
noOfCustomers=0
#in this for loop one by one customers are checked to see if they can be included
for i in range(no):
    c=compareList[i][0]
    def check():
        global inlist,outlist
        for j in range(len(dislikeList[c])):
            if dislikeList[c][j] in inlist: #if they dislike something that is liked by previous ones
                return 0
        for j in range(len(likeList[c])): #if they like something that is disliked by previous ones
            if likeList[c][j] in outlist:
                return 0
        for j in range(len(likeList[c])): #if they are eligible
            inlist+=[likeList[c][j]]
        for j in range(len(dislikeList[c])):
            outlist+=[dislikeList[c][j]]
        return 1
    # check()
    if check():
        noOfCustomers+=1
inlist=list(set(inlist))
inlist=[noOfCustomers]+[len(inlist)]+inlist
print(*inlist)
 