# coding:utf-8
import cookielib
import os
import requests


def save_cookies(session, username):
    new_cookie_jar = cookielib.LWPCookieJar(username + '.txt')
    # 将转换成字典格式的RequestsCookieJar（这里我用字典推导手动转的）保存到LWPcookiejar中
    requests.utils.cookiejar_from_dict(
        {c.name: c.value
         for c in session.cookies}, new_cookie_jar)
    # 保存到本地文件
    if not os.path.exists('cookies'):
        os.mkdir('cookies')
    new_cookie_jar.save(
        'cookies/' + username + '.txt',
        ignore_discard=True,
        ignore_expires=True)


def read_cookies(username):
    # 实例化一个LWPCookieJar对象
    load_cookiejar = cookielib.LWPCookieJar()
    # 从文件中加载cookies(LWP格式)
    load_cookiejar.load(
        'cookies/' + username + '.txt',
        ignore_discard=True,
        ignore_expires=True)
    # 工具方法转换成字典
    load_cookies = requests.utils.dict_from_cookiejar(load_cookiejar)
    # 工具方法将字典转换成RequestsCookieJar，赋值给session的cookies.
    # print session.text
    return requests.utils.cookiejar_from_dict(load_cookies)