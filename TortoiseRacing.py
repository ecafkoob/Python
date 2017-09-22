#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Author:贾江超

def race(v1, v2, g):
    if v1 >= v2:
        return None
    v1=float(v1)
    v2 = float(v2)
    g = float(g)
    x=g/(v2-v1)
    h=int(g//(v2-v1))
    m=int((x-h)*60//1)
    s=int((x*3600-h*60*60-m*60)//1)
    if s==60:
        m=m+1
        s=0
        if m==60:
            h+=1
            m=0
    return [h,m,s]