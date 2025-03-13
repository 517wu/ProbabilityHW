import random
def getnum():
    a=[]
    for i in range(10):
        a.append(random.randint(0,9))#1:red,0:yellow
    return a

bag_R={'A':1/5,'B':1/2,'C':7/10,'D':9/10,'E':3/10}
print("每一袋的機率: ",end="")
for i in bag_R:
    print(f"{i}:{bag_R.get(i)}",end=" ")
print()
bag_index=[2,5,7,9,3]
anslist={2:'A',5:'B',7:'C',9:'D',3:'E'}
random.shuffle(bag_index)
ans=[]
for i in bag_index:
    ans.append(anslist.get(i))
print(ans)
Rlist=[]
Ylist=[]
bag=[]
x=[]
t=0
while x!=ans:
    if t>0:
        for i in bag:
            i.extend(getnum())
    else:
        for i in range(5):
            bag.append(getnum())
    t+=1
    for a in bag:
        R=Y=0
        for i in a:
            
            if i>=bag_index[bag.index(a)]:
                R+=1
            else:
                Y+=1
        Rlist.append(R)
        Ylist.append(Y)
        print(f"第{bag.index(a)+1}袋: R:{R} Y:{Y}")
        p=R/len(a)
        print(p)
        # close=1
        # target=0
        # for i in bag_R:
        #     c=bag_R.get(i)
        #     if(abs(p-c)<close):
        #         close=abs(p-c)
        #         target=i
        # print(target)
    x=input("請猜分別是哪一袋: ").upper().split()
    print(x)
print("finish")
