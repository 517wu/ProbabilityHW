from math import factorial
import random
def ANS():
  ans=''
  for i in range(2):
    a=str(random.randint(0,9))
    if i>0:
     for j in ans:
       while j==a:
          a=str(random.randint(0,9))
    ans+=a
  return ans

def repeat(X):
    a=X.count(X[0])
    if a>1:
      return True
    else:
        return False

def countAB(X,ans):
  A=B=0
  for i in range(0,2):
    for j in range(0,2):
      if X[i]==ans[j]:
        if i==j:
          A+=1
        else:
          B+=1
  return A,B

def c(x,y):
    return factorial(x)//(factorial(x-y)*factorial(y))

A=B=t=0
ans=ANS()
inputlist=set()
print("歡迎來玩 1A2B!!")
print("若想放棄本局請輸入-1")

numlist=['0','1','2','3','4','5','6','7','8','9']#記可能的數
aknownlist=[]#記1A的結果
bknownlist=[]#記1B的結果
check=2 #確定的格數
change=2#是否交換位置(2:yes 1:no)
while A!=2:
    t+=1
    print(f"這是你第{t}次輸入，",end='')
    X=input("請輸入二位數字: ")
    if X=="-1":
        break
    elif X<"0" or X>"98" or repeat(X) or (X in inputlist):
        print("輸入錯誤!!")
        t-=1
        continue
    inputlist.add(X)
    A,B=countAB(X,ans)
    
    type=(A,B)
    match type:
        case (x,y) if x==2:
            break
        case (x,y) if y==2:
            numlist=[X[0],X[1]]
            check=0
            change=1
        case (x,y) if x==y==0:
            if X[0] in numlist:
                numlist.remove(X[0]) 
            if X[1] in numlist:
                numlist.remove(X[1])
            if aknownlist:
                for a in aknownlist:
                    if X[0]==a[0]:
                        check=1
                        if a[1] in numlist:
                            numlist.remove(a[1])
                        change=1
                    elif X[1]==a[1]:
                        check=1
                        if a[0] in numlist:
                            numlist.remove(a[0])
                        change=1
            if bknownlist:
                for b in bknownlist:
                    if X[0]==b[1] and X[1]!=b[0]:
                        check=1
                        if b[0] in numlist:
                            numlist.remove(b[0])
                        change=1
                    elif X[1]==b[0] and X[0]!=b[1]:
                        check=1
                        if b[1] in numlist:
                            numlist.remove(b[1])
                        change=1
            if len(numlist)==0:
                check=0  
        case (x,y) if y==1:
            check=1
            if X[0] in numlist:
                numlist.remove(X[0]) 
            if X[1] in numlist:
                numlist.remove(X[1])
            if aknownlist:
                change=1
                for a in aknownlist:
                    if len({X[0],X[1],a[0],a[1]})==2:
                        change=2
                    elif X[0]==a[0]:
                        numlist.remove(a[1])   
                        check=0
                    elif X[1]==a[1]:
                        numlist.remove(a[0])
                        check=0
                    elif X[0]==a[1] and X[1]!=a[0]:
                        numlist.remove(a[0])
                    elif X[1]==a[0] and X[0]!=a[1]:
                        numlist.remove(a[1])
                    elif len({X[0],X[1],a[0],a[1]})==4:
                        numlist=[X[0],X[1]]
            if bknownlist:
                change=1
                for b in bknownlist:
                    if X[0]==b[1] and X[1]!=b[0]:
                        check=0
                    elif X[1]==b[0] and X[0]!=b[1]:
                        check=0
                    elif X[0]==b[0]:
                       numlist.remove(b[1])
                    elif X[1]==b[1]:
                       numlist.remove(b[0])
                    elif len({X[0],X[1],b[0],b[1]})==4:
                        numlist=[X[0],X[1]]
            bknownlist.append(X)
        case (x,y) if x==1:
            check=1
            if X[0] in numlist:
                numlist.remove(X[0]) 
            if X[1] in numlist:
                numlist.remove(X[1])
            if aknownlist:
                change=1
                for a in aknownlist:
                    if X[0]==a[0]:
                        numlist.remove(a[1])   
                    elif X[1]==a[1]:
                        numlist.remove(a[0])
                    elif X[0]==a[1] and X[1]!=a[0]:
                        check=0
                    elif X[1]==a[0] and X[0]!=a[1]:
                        check=0
                    elif len({X[0],X[1],a[0],a[1]})==4:
                        numlist=[X[0],X[1]]
            if bknownlist:
                change=1
                for b in bknownlist:
                    if len({X[0],X[1],b[0],b[1]})==2:
                        change=2
                    elif X[0]==b[1] and X[1]!=b[0]:
                        numlist.remove(b[0])
                    elif X[1]==b[0] and X[0]!=b[1]:
                        numlist.remove(b[1])
                    elif X[0]==b[0]:
                       check=0
                    elif X[1]==b[1]:
                       check=0
                    elif len({X[0],X[1],b[0],b[1]})==4:
                        numlist=[X[0],X[1]]
            aknownlist.append(X)
    
    

    print(f"{A}A{B}B",end="\t")
    print(aknownlist,bknownlist,check,change,numlist)
    if A!=2:
        p=c(len(numlist),check)*change
        print(f"猜中機率:{1/p:.4f} (剩下{p}種可能)")
    

if X=="-1":
  print("公布答案: ",ans)
else:
  if t<=6:
    print(f"\n你好厲害，只花了{t}次")
  else:
    print(f"\n辛苦了，花了{t}次")