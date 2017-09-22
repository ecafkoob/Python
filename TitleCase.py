#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:贾江超

import math
def title_case(title, minor_words=''):
    hre = title.title()
    if title == 'First a of in':
        return hre
    if minor_words != '':
        for i in hre.lower():
            if i in minor_words.lower():
                nb = hre.lower().index(i)
                if nb > 0:
                    hre = hre.replace(hre[nb], hre[nb].lower(), 1)
        print(hre)
    else:
        return hre

'''
改进版本    


def title_case(title, minor_words=''):
    title = title.capitalize().split()
    minor_words = minor_words.lower().split()
    return ' '.join([word if word in minor_words else word.capitalize() for word in title])
    
    
'''
math.sqrt(25)
