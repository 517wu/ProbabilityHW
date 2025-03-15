import random
def getnum():
    a=[]
    for i in range(5):
        a.append(random.randint(0,9))#一袋10個，依比例區分紅黃
    return a

print("小明有 A ~ E 五個袋子，每個袋子有的紅黃球比例不一，\n由於年代久遠袋子上的標示已無法看清，但小明手上有五個袋子的紅黃球個數列表，請幫助小明辨別每個袋子。")
print("\n以下是五個袋子的紅黃球比例: ")
print("A袋：紅球 x 2 黃球 x 8")
print("B袋：紅球 x 5 黃球 x 5")
print("C袋：紅球 x 7 黃球 x 3")
print("D袋：紅球 x 9 黃球 x 1")
print("E袋：紅球 x 3 黃球 x 7")
print("\n現在從五個袋子中分別抽出五顆球，請幫小明猜出對應的袋子名稱。(輸入範例：abcde，若要放棄請輸入-1)")

bag_index=[2,5,7,9,3]
anslist={2:'A',5:'B',7:'C',9:'D',3:'E'}
random.shuffle(bag_index)
ans=""
for i in bag_index:
    ans+=anslist.get(i)
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
            if i<bag_index[bag.index(a)]:
                R+=1
            else:
                Y+=1
        Rlist.append(R)
        Ylist.append(Y)
        print(f"第{bag.index(a)+1}袋: R:{R} Y:{Y}")
        p=R/len(a)
        print(f"紅球佔其中的比例：{p:.4g}")
    x=input("請猜分別是哪一袋: ").upper()
    if x=='-1':
        break
if x!='-1':
    print(f"恭喜你在第{t}次猜對了!!")
print("答案為："+ans)
