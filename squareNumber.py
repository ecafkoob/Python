#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:贾江超


def square_digits(num):
    s = str(num)
    result = []
    for i in s:
        n = int(i)
        pf = n ** 2
        string = str(pf)
        result.append(string)
        re = int(''.join(result))
    return re

'''
进阶版本 def square_digits(num):
            return int(''.join(str(int(d)**2) for d in str(num)))
'''