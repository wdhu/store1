import random
num = random.randint(0,1000)
count = 0
m = 5000
while True:
    count = count+1
    chose = input("请输入您要猜的数字")
    chose = int(chose)
    if chose > num:
        print("大了！")
        m = m - 500
        print("由于您猜错了扣除您500硬币，您的硬币余额为", m)
    elif chose < num:
        print("小了！")
        m = m-500
        print("由于您猜错了扣除您500硬币，您的硬币余额为",m)
    elif m < 500:
        print("抱歉，您的余额不足")
        break
    else:
        print("恭喜您猜中了，本次数字为",num,"您总共猜了",count,"次")
        m = m+10000
        print("您获得本次奖励10000硬币，您的硬币余额为",m,"是否进入第二轮")
        break