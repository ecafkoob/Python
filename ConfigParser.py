# encoding: utf-8
"""
@author: ecafkoob 
@contact: a654747873@gmail.com
@site: www.zzxxxc.cn
@version: 1.0
@license: Apache Licence
@file: ConfigParser.py
@time: 17-12-11 下午5:24

"""
import configparser

config = configparser.ConfigParser()
config = configparser.ConfigParser()
config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'  # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('sample.ini','w') as f:
    config.write(f)


def run():
    pass


if __name__ == '__main__':
    run()
