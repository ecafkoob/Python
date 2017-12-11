# encoding: utf-8
"""
@author: ecafkoob 
@contact: a654747873@gmail.com
@site: www.zzxxxc.cn
@version: 1.0
@license: Apache Licence
@file: configparserdemo.py
@time: 17-12-11 下午5:39

"""
import configparser

cf = configparser.ConfigParser()
#
# cf['services'] = {'ip': '127.0.0.1',
#                   'hostname': 'localhost',
#                   'operatingsystem': 'windows'
#
#                   }
# cf['machine'] = {}
# cf['machine']['cpu'] = 'intel i7'
# cf['machine']['mem'] = 'samsun'
# cf['network'] ={}
# net = cf['network']
# net['router'] = 'huawei'
# net['swaper'] = 'cisco'
# with open('server-conf.ini', 'w') as conf:
#     cf.write(conf)
#
#
# def run():
#     pass
#
#
# if __name__ == '__main__':
#     run()

print(cf.sections())
cf.read('sample.ini')
print(cf.sections())
print(cf['DEFAULT'])
for key in cf['bitbucket.org']: print(key)
print(cf['bitbucket.org']['user'])
'''
configparser的sections的 名字不区分大小写 都以小写的方式保存 default段的 k-v对会给其他字段提供默认值
'''