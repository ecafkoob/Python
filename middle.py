#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Author:贾江超
def middle(str):
    l=len(str)
    if l%2!=0:
        a=l//2
        mid=str[a]
    else :
        b=l//2
        mid=str[b-1]+str[b]
    return mid




