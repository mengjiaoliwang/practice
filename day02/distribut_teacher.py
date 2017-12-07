#!/usr/bin/python
#coding=utf-8
'''*************************************************************************
	> File Name: distribut_teacher.py
	> Author:李梦娇 
	> Mail:mengjao_liwang@yeah.net 
	> Created Time: 2017年12月07日 星期四 10时13分15秒
 ************************************************************************'''
import random

offices=[[],[],[]]

teachersname=['A','B','C','D','E','F','G','H']
#随机分配老师
for name in teachersname:
    index=random.randint(0,2)#在0,2之间产生随机数
    offices[index].append(name)
i=1
for tempoffice in offices:
    print("第%d办公室的人有%d个"%(i,len(tempoffice)))
    i+=1
    for name in tempoffice: 
        print(name,end=" ")
    print()
    print("*"*20)
