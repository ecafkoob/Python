from urllib import request, parse

url = "http://httpbin.org/get"

parms = {
    'name1': 'value1',
    'name2': 'value2'
}
# Encode the query string
querystring = parse.urlencode(parms)
# Make a GET request and read the response
u = request.urlopen(url + '?' + querystring)
resp = u.read()
'''
网络编程主要是分为rest接口编程还有些一些调用底层网络协议的编程，系统编程的一部分
会用到的知识tcp ip 的知识 还有序列化的少许内容 重点是 http 协议  request and response
等等 向现有框架比如 django flask等等都有涉及到网络底层的编程不过一般要求不高，底层的东西一般不会去动
了解就可以了
'''