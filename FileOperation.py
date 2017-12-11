# encoding: utf-8
"""
@author: ecafkoob 
@contact: a654747873@gmail.com
@site: www.zzxxxc.cn
@version: 1.0
@license: Apache Licence
@file: FileOperation.py
@time: 17-12-11 下午2:59
python 的文件对象 主要用迭代器遍历特定的行，
"""
import sys, time

'''
for i in range(100):
    sys.stdout.write('#')
    sys.stdout.flush()  # 把缓冲区的内容直接刷到终端
    time.sleep(0.1)  # 让显示有间隔不然太快太突兀
'''
with open('yesterday', 'r') as f:
    print('===================================================')
    print(f.read(100))
    print(f.tell())
    print('===================================================')
    f.seek(100)
    print(f.readline())
    print(f.tell())
    print('===================================================')
    f.seek(0)
    print(f.readlines())
    print(len(f.readlines()))
    f.close()

