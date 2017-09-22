#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Author:贾江超

def accum(s):
    slower=s.lower()
    l=list(slower)
    length=len(l)
    result=[]
    for i in range(length):
        time=i+1
        result.append('-')
        for j in range(time) :
            result.append(slower[i])
    result.pop(0)
    result1=''.join(result)
    title=result1.title()
    return title

'''
一个牛逼的版本

def accum(s):
    return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))
'''