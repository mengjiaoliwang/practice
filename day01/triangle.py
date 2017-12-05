#!/usr/bin/python
#coding=utf-8
'''*************************************************************************
	> File Name: triangle.py
	> Author:李梦娇 
	> Mail:mengjao_liwang@yeah.net 
	> Created Time: 2017年12月05日 星期二 19时47分07秒
 ************************************************************************'''
i=1
while i<=5:
    j=1
    while j<=i:
        print "* ",#python不换行
        #print("* ",end=" ")#Python3不换行
        j+=1
    i+=1
    print("\n")
while i>=0:
    j=1
    while j<i:
         print "* ",
        #print("* ",end=" ")
         j+=1
    i-=1
    print("\n")

