#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:贾江超\
'''
Scramblies

Write function scramble(str1,str2) that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

For example:
str1 is 'rkqodlw' and str2 is 'world' the output should return true.
str1 is 'cedewaraaossoqqyt' and str2 is 'codewars' should return true.
str1 is 'katas' and str2 is 'steak' should return false.

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered
'''


def scramble(str1, str2):
    for i in str2:
        if i not in str1:
            return False
    if set(str2).issubset(set(str1)):
        for j in ''.join(set(str2)):
            if list(str2).count(j) == list(str1).count(j):
                pass
            elif list(str2).count(j) <=list(str1).count(j):
                return False
    return True
'''
来一个使用了collections库的高端方法 使用collections.Counter()方法获得一个关于字符和个数的字典
用s2的字典来减去s1的字典然后如果长度为0那就说明ok 妙实在是妙啊

'''
'''
from collections import Counter
def scramble(s1,s2):
    # Counter basically creates a dictionary of counts and letters
    # Using set subtraction, we know that if anything is left over,
    # something exists in s2 that doesn't exist in s1
    return len(Counter(s2)- Counter(s1)) == 0

from collections import Counter
I V X L C D M
'''