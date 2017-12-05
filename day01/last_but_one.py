#!/usr/bin/python
#coding=utf-8
'''*************************************************************************
	> File Name: last_but_one.py
	> Author:李梦娇 
	> Mail:mengjao_liwang@yeah.net 
	> Created Time: 2017年12月05日 星期二 20时49分09秒
 ************************************************************************'''
teststr="haha nihao a \t heihei \t woshi nide \t hao \npengyou"
teststr.split("\t")
print(teststr.split("\t")[len(teststr.split("\t"))-2])
