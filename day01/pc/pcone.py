#要求：从键盘输入刀子的长度，如果刀子长度没有超过10cm，则
# 允许上火车，否则不允许上火车
length=input("请输入刀子的长度")

if int(length)>=10:
    print("刀子过长，不能上车")
else:
    print("可以上车")