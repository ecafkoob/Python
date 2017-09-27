#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:贾江超
def narcissistic(value):
    return True if sum(([pow(i,len(str(value))) for i in list(map(int,str(value)))])) ==value else False
