#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:贾江超
def narcissistic(value):
    strNum = str(value)
    l = len(strNum)
    num = int(strNum)
    sum = 0
    for i in range(0, l):
        a = int(strNum[i]) ** l
        sum = a + sum
    return sum==num

