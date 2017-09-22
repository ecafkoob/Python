#!/usr/bin/env python3
#-*- coding:utf-8 -*-
#Author:贾江超

def goodVsEvil(good, evil):
    arrgood=[i for i in list(good) if i !=' ']
    arrbad=[i for i in list(evil) if i !=' ']
    goodvalue=[1,2,3,3,4,10]
    badvalue=[1,2,2,2,3,5,10]
    sumgood=0
    sumbad=0
    for i in range(6):
        sumgood+=(int(arrgood[i]))*goodvalue[i]
    for j in range(7):
        sumbad+=(int(arrbad[j]))*badvalue[j]
    if sumgood > sumbad:
        return 'Battle Result: Good triumphs over Evil'
    if sumgood < sumbad:
        return "Battle Result: Evil eradicates all trace of Good"
    if sumgood == sumbad:
        return "Battle Result: No victor on this battle field"

    list.remove()