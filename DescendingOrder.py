#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:贾江超


def descendingOrder(value):
    raw = str(value)
    l = len(raw)
    list1 = list(raw)
    list1.reverse()
    re = ''.join(list1)
    list.sort(reverse=True)
    return int(re)

Input: 1254859723 Output: 9875543221