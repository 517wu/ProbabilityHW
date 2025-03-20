from guessbag import guess
import random
print("本場遊戲為「瘋狂旋轉」！！可選的下注項目為：")
print("* 2的倍數")
print("* 3的倍數")
print("* 4的倍數")
print("* 6的倍數")
print("* 9的倍數")
print("* 12的倍數")
print("* 18的倍數")
print("* 36的倍數")
money=10000
while True:
    print(f"\n目前錢包內的金額{money}元")
    c=input("要下注嗎？(yes/no): ").lower()
    while True:
        if (c!='no' and c!='yes'):
            print("輸入錯誤!!")
            c=input("請再輸入一次：(yes/no)").lower()
            continue
        elif c=='no':
            print('您已退出本場遊戲，歡迎下次光臨！！')
            break
        elif (c=='yes' and money<=0):
            c=input('是否幫小明一個忙，來打工賺錢?(yes/no)').lower()
            if (c!='no' and c!='yes'):
                continue
            elif c=='no':
                print('本場遊戲不支援空手套白狼，歡迎下次備妥現金光臨！！') 
                break
            else:
                guess()
                print("小明為了感謝你的幫忙，給了500元作為報酬")
                money+=500  
                print(f"\n目前錢包內的金額{money}元")
        break
    if c=="no":
        break   
    chose=[2,3,4,6,9,12,18,36]
    while True:
        type=int(input("請輸入你要下注的倍數："))
        if type in chose:
            break
        print("輸入錯誤！！請再輸入一次")
    while True:
        x=int(input("輸入下注金額："))
        if x<=money:
            break
        print("餘額不足！！請再輸入一次")
    ans=random.randint(1,36)
    print(f'本次輪盤的結果為：{ans}號')
    if ans%type!=0:
        print(f"玩家扣除{x}元")
        money-=x
    else:
        print(f"玩家獲得{x*type}元")
        money+=(x*type)