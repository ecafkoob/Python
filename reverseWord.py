#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Author:贾江超

def spin_words(sentence):
    list1=sentence.split()
    l=len(list1)
    for i in range(l):
        relen = len(sentence.split()[i:][0])
        if relen > 5:
           list1[i]=list1[i][::-1]
    return ' '.join(list1)

'''
注意 在2.x版本可以用len()得到list的长度 3.x版本就不行了

优化版本  

def spin_words(sentence):
    # Your code goes here
    return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
    
    在这里倒序字符串用切片很方便 str[::-1] 就ok了
'''

