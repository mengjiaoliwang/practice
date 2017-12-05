#!/usr/bin/python
#coding=utf-8
'''*************************************************************************
	> File Name: reversed_order.py
	> Author:李梦娇 
	> Mail:mengjao_liwang@yeah.net 
	> Created Time: 2017年12月05日 星期二 20时21分35秒
 ************************************************************************'''

orderstr=input('请输入字符串')
strlen=len(orderstr)
i=0
print(orderstr[strlen-1-i:0:-1],end=orderstr[0])
print("")
#print(orderstr[0])
