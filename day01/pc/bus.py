''''
情节描述：上公交车，并且可以有座位坐下

要求：输入公交卡当前的余额，只要超过2元，
就可以上公交车；如果空座位的数量大于0，就可以坐下
'''''
money=input("公交车剩余的钱数为：")
seat=input("剩余的座位为：")
if int(money)>2:
    print("可以上车")
    if int(seat)>0:
        print("有座位")
    else:
        print("无座位")
else:
    print("公交卡上的余额不足")