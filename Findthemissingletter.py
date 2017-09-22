#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:贾江超


def find_missing_letter(chars):
    ordArr = [ord(x) for x in chars]
    l = len(ordArr)
    for i in range(l - 1):
        result = ordArr[i + 1] - ordArr[i]
        if result == 1:
            pass
        else:
            re = chr(ordArr[i] + 1)
    return re


'''
优化的版本
def find_missing_letter(c):
    return next(chr(ord(c[i])+1) for i in range(len(c)-1) if ord(c[i])+1 != ord(c[i+1]))
'''
