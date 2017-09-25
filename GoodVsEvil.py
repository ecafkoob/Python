#!/usr/bin/env python3
# -*- coding:utf-8 -*-
# Author:贾江超


def goodVsEvil(good, evil):
    arrgood = [i for i in list(good) if i != ' ']
    arrbad = [i for i in list(evil) if i != ' ']
    goodvalue = [1, 2, 3, 3, 4, 10]
    badvalue = [1, 2, 2, 2, 3, 5, 10]
    sumgood = sum([int(x) * y for x, y in zip(good.split(), goodvalue)])
    sumbad= sum([int(x) * y for x, y in zip(evil.split(), badvalue)])
    if sumgood > sumbad:
        return 'Battle Result: Good triumphs over Evil'
    if sumgood < sumbad:
        return "Battle Result: Evil eradicates all trace of Good"
    if sumgood == sumbad:
        return "Battle Result: No victor on this battle field"


def goodVsEvil(good, evil):
    points_good = [1, 2, 3, 3, 4, 10]
    points_evil = [1, 2, 2, 2, 3, 5, 10]

    good = sum([int(x) * y for x, y in zip(good.split(), points_good)])
    evil = sum([int(x) * y for x, y in zip(evil.split(), points_evil)])

    result = 'Battle Result: '

    if good < evil:
        return result + 'Evil eradicates all trace of Good'
    elif good > evil:
        return result + 'Good triumphs over Evil'
    else:
        return result + 'No victor on this battle field'