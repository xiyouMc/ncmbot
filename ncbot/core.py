# coding:utf-8
"""
    NCloudBot.core
    ~~~~~~~~~~~~~~
    This module implements the main NCloudBot system.

    :copyright: (c) 2017 by xiyouMc.
    :license: ISC, see LICENSE for more details.
"""
import hashlib
import requests
import json
import cookielib
import traceback
from .util.encrypt import encrypted_request
from .util import cookiesJar
from utils import get_encoding_from_headers

__title__ = 'ncbot'
__version__ = '0.1.0'
__build__ = 0x000100
__author__ = 'XiyouMc'
__license__ = 'ISC'
__copyright__ = 'Copyright 2017 XiyouMc'


class NCloudBot(object):
    """
    The :class:`NCloudBot` object. It carries out all functionality of 
    NCloudBot 
    Recommended interface is with the NCloudBot`s functions.
    """
    req = requests.Session()
    username = None
    _METHODS = {
        # 登录模块
        'LOGIN': '/weapi/login/cellphone?csrf_token=',
        # 获取用户信息
        'USER_INFO': '/weapi/subcount',
        # 获取用户歌单,收藏的歌单 , 指定 UserId , 不需要登录
        'USER_PLAY_LIST': '/weapi/user/playlist',
        # 获取用户电台
        'USER_DJ': '/weapi/dj/program/%s',
        # 获取用户关注列表
        'USER_FOLLOWS': '/weapi/user/getfollows/%s',
        # 获取用户粉丝
        'USER_FOLLOWEDS': '/weapi/user/getfolloweds/',
        # 获取用户动态
        'USER_EVENT': '/weapi/event/get/%s',
        # 获取用户播放记录
        'USER_RECORD': '/weapi/v1/play/record',
        # 获取各种动态，对应网页版网易云，朋友界面的各种动态消息，如分享的视频、音乐、照片等
        'EVENT': '/weapi/v1/event/get',
        # 获取精品歌单
        'TOP_PLAYLIST_HIGHQUALITY': '/weapi/playlist/highquality/list',
        # 传入歌单ID 获取对应歌单内的所有音乐
        'PLAY_LIST_DETAIL': '/weapi/v3/playlist/detail',
        # 传入音乐ID ,获取对应音乐的URL
        'MUSIC_URL': '/weapi/song/enhance/player/url',
        # 传入关键词，获取歌曲列表
        'SEARCH': '/api/search/get/',
        # 传入音乐ID，获取对应音乐的歌词
        'LYRIC': '/api/song/lyric?os=osx&id=%s&lv=-1&kv=-1&tv=-1',
        # 传入音乐ID 和 limit 参数，可获取该音乐的所有评论
        'MUSIC_COMMENT': '/weapi/v1/resource/comments/R_SO_4_%s/?csrf_token=',
        # 传入专辑ID 和 limit 参数，可获取该专辑的所有评论
        'ALBUM_COMMENT': '/weapi/v1/resource/comments/R_AL_3_%s/?csrf_token=',
        # 给评论点赞,入参是资源ID，如歌曲ID，MV iD 和 评论ID
        'LIKE_COMMENT': '/weapi/v1/comment/%s',
        # 传入音乐ID,获取歌曲详情
        'SONG_DETAIL': '/weapi/v3/song/detail',
        # 获取专辑内容
        'ALBUM': '/weapi/v1/album/%s',
        # 私人 FM （需要登录）
        'PERSONAL_FM': '/weapi/v1/radio/get'
    }

    __NETEAST_HOST = 'http://music.163.com'

    def __init__(self):
        self.method = None
        self.data = {}
        self.params = {}
        self.response = Response()

    def __repr__(self):
        return '<Request [%s]>' % (self.method)

    def __setattr__(self, name, value):
        if (name == 'method') and (value):
            if value not in self._METHODS.keys():
                raise InvalidMethod()
        object.__setattr__(self, name, value)

    def _get_webapi_requests(self):
        headers = {
            'Accept':
            '*/*',
            'Accept-Language':
            'zh-CN,zh;q=0.8,gl;q=0.6,zh-TW;q=0.4',
            'Connection':
            'keep-alive',
            'Content-Type':
            'application/x-www-form-urlencoded',
            'Referer':
            'http://music.163.com',
            'Host':
            'music.163.com',
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'
        }
        NCloudBot.req.headers.update(headers)
        return NCloudBot.req

    def _get_requests(self):
        headers = {
            'Referer':
            self.__NETEAST_HOST,
            'Cookie':
            'appver=2.0.2;',
            'Content-Type':
            'application/x-www-form-urlencoded',
            'User-Agent':
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/33.0.1750.152 Safari/537.36'
        }

        NCloudBot.req.headers.update(headers)
        return NCloudBot.req

    def _build_response(self, resp):
        # rememberLogin
        # if self.method is 'LOGIN' and resp.json().get('code') == 200:
        #     cookiesJar.save_cookies(resp, NCloudBot.username)
        self.response.content = resp.content
        self.response.status_code = resp.status_code
        self.response.headers = resp.headers

    def send(self):
        success = False
        if self.method is None:
            raise ParamsError()
        try:
            if self.method == 'SEARCH':
                req = self._get_requests()
                _url = self.__NETEAST_HOST + self._METHODS[self.method]
                resp = req.post(_url, data=self.data)
                self._build_response(resp)
                self.response.ok = True
            else:
                if isinstance(self.data, dict):
                    data = encrypted_request(self.data)

                req = self._get_webapi_requests()
                _url = self.__NETEAST_HOST + self._METHODS[self.method]

                if self.method in ('USER_DJ', 'USER_FOLLOWS', 'USER_EVENT'):
                    _url = _url % self.params['uid']

                if self.method in ('LYRIC', 'MUSIC_COMMENT'):
                    _url = _url % self.params['id']
                # GET
                if self.method in ('LYRIC'):
                    resp = req.get(_url)
                else:
                    resp = req.post(_url, data=data)
                self._build_response(resp)
                self.response.ok = True
        except Exception as why:
            traceback.print_exc()
            print 'Requests Exception', why
            # self._build_response(why)
            self.response.error = why


class Response(object):
    def __init__(self):
        self.content = None
        self.headers = None
        self.status_code = None
        self.ok = False
        self.error = None

    def __repr__(self):
        return '<Response [%s]>' % (self.status_code)

    def raise_for_status(self):
        if self.error:
            raise self.error

    def json(self):
        """Returns the json-encoded content of a response, if any."""

        if not self.headers and len(self.content) > 3:
            encoding = get_encoding_from_headers(self.headers)
            if encoding is not None:
                return json.loads(self.content.decode(encoding))
        return json.loads(self.content)


def login(password, phone=None, email=None, rememberLogin=True):
    if (phone is None) and (email is None):
        raise ParamsError()
    if password is None:
        raise ParamsError()
    r = NCloudBot()
    # r.username = phone or email
    r.method = 'LOGIN'
    md5 = hashlib.md5()
    md5.update(password)
    password = md5.hexdigest()
    print password
    r.data = {'password': password, 'rememberLogin': rememberLogin}
    if phone is not None:
        r.data['phone'] = phone
    else:
        r.data['username'] = email
    r.send()

    return r.response


def user_play_list(uid, offset=0, limit=1000):
    if uid is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'USER_PLAY_LIST'
    r.data = {'offset': offset, 'uid': uid, 'limit': limit, 'csrf_token': ''}
    r.send()
    return r.response


def user_dj(uid, offset=0, limit=30):
    if uid is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'USER_DJ'
    r.data = {'offset': offset, 'limit': limit, "csrf_token": ""}
    r.params = {'uid': uid}
    r.send()

    return r.response


def search(keyword, type=1, offset=0, limit=30):
    if keyword is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'SEARCH'
    r.data = {
        's': keyword,
        'limit': str(limit),
        'type': str(type),
        'offset': str(offset)
    }
    r.send()

    return r.response


def user_follows(uid, offset='0', limit=30):
    if uid is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'USER_FOLLOWS'
    r.params = {'uid': uid}
    r.data = {'offset': offset, 'limit': limit, 'order': True}
    r.send()

    return r.response


def user_followeds(uid, offset='0', limit=30):
    if uid is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'USER_FOLLOWEDS'
    r.data = {
        'userId': uid,
        'offset': offset,
        'limit': limit,
        "csrf_token": ""
    }
    r.send()

    return r.response


def user_event(uid):
    if uid is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'USER_EVENT'
    r.params = {'uid': uid}
    r.data = {'time': -1, 'getcounts': True, "csrf_token": ""}
    r.send()

    return r.response


def user_record(uid, type=0):
    if uid is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'USER_RECORD'
    r.data = {'type': type, 'uid': uid, "csrf_token": ""}
    r.send()

    return r.response


def event():
    r = NCloudBot()
    r.method = 'EVENT'
    r.data = {"csrf_token": ""}
    r.send()

    return r.response


# TOP_PLAYLIST_HIGHQUALITY
def top_playlist_highquality(cat='全部', offset=0, limit=20):
    r = NCloudBot()
    r.method = 'TOP_PLAYLIST_HIGHQUALITY'
    r.data = {'cat': cat, 'offset': offset, 'limit': limit}
    r.send()

    return r.response


# PLAY_LIST_DETAIL
def play_list_detail(id, limit=20):
    if id is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'PLAY_LIST_DETAIL'
    r.data = {'id': id, 'limit': limit, "csrf_token": ""}
    r.send()

    return r.response


# MUSIC_URL
def music_url(ids=[]):
    if not isinstance(ids, list):
        raise ParamsError()
    r = NCloudBot()
    r.method = 'MUSIC_URL'
    r.data = {'ids': ids, 'br': 999000, "csrf_token": ""}
    r.send()

    return r.response


# LYRIC
def lyric(id):
    if id is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'LYRIC'
    r.params = {'id': id}
    r.send()

    return r.response


# MUSIC_COMMENT
def music_comment(id, offset=0, limit=20):
    if id is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'MUSIC_COMMENT'
    r.params = {'id': id}
    r.data = {'offset': offset, 'limit': limit, 'rid': id, "csrf_token": ""}
    r.send()

    return r.response


# ALBUM_COMMENT
def album_comment(id, offset=0, limit=20):
    if id is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'ALBUM_COMMENT'
    r.params = {'id': id}
    r.data = {'offset': offset, 'limit': limit, 'rid': id, "csrf_token": ""}
    r.send()

    return r.response


# SONG_DETAIL
def song_detail(ids):
    if not isinstance(ids, list):
        raise ParamsError()
    c = []
    for id in ids:
        c.append({'id': id})
    r = NCloudBot()
    r.method = 'SONG_DETAIL'
    r.data = {'c': json.dumps(c), 'ids': c, "csrf_token": ""}
    r.send()

    return r.response


# PERSONAL_FM
def personal_fm():
    r = NCloudBot()
    r.method = 'PERSONAL_FM'
    r.data = {"csrf_token": ""}
    r.send()
    return r.response


class NCloudBotException(Exception):
    """ 这是 NCloudBot 当处理请求时候的异常"""


class ParamsError(NCloudBotException):
    """ 参数错误 """


class InvalidMethod(NCloudBotException):
    """ 不支持的方法被调用"""