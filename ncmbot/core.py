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

__title__ = 'ncmbot'
__version__ = '0.1.0'
__build__ = 0x000100
__author__ = 'XiyouMc'
__license__ = 'ISC'
__copyright__ = 'Copyright 2017 XiyouMc'

__all__ = [
    'NCloudBot', 'Response', 'login', 'user_play_list', 'user_dj', 'search',
    'user_follows', 'user_followeds', 'user_event', 'event',
    'top_playlist_highquality', 'play_list_detail', 'music_url', 'lyric',
    'music_comment', 'song_detail', 'personal_fm', 'user_record'
]


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
        # 邮箱登录
        'EMAIL_LOGIN': '/weapi/login?csrf_token=',
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
        return '<NCloudBot [%s]>' % (self.method)

    def __setattr__(self, name, value):
        if (name == 'method') and (value):
            if value not in self._METHODS.keys():
                raise InvalidMethod()
        object.__setattr__(self, name, value)

    def _get_webapi_requests(self):
        """Update headers of webapi for Requests."""

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
        """Build internal Response object from given response."""
        # rememberLogin
        # if self.method is 'LOGIN' and resp.json().get('code') == 200:
        #     cookiesJar.save_cookies(resp, NCloudBot.username)
        self.response.content = resp.content
        self.response.status_code = resp.status_code
        self.response.headers = resp.headers

    def send(self):
        """Sens the request."""
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
    """
    The :class:`Response` object. All :class:`NCloudBot` objects contain a 
    :class:`NCloudBot.response <response>` attribute.
    """

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
    """ 登录接口，返回 :class:'Response' 对象
    :param password: 网易云音乐的密码
    :param phone: (optional) 手机登录
    :param email: (optional) 邮箱登录
    :param rememberLogin: (optional) 是否记住密码，默认 True
    """
    if (phone is None) and (email is None):
        raise ParamsError()
    if password is None:
        raise ParamsError()
    r = NCloudBot()
    # r.username = phone or email

    md5 = hashlib.md5()
    md5.update(password)
    password = md5.hexdigest()
    print password
    r.data = {'password': password, 'rememberLogin': rememberLogin}
    if phone is not None:
        r.data['phone'] = phone
        r.method = 'LOGIN'
    else:
        r.data['username'] = email
        r.method = 'EMAIL_LOGIN'
    r.send()

    return r.response


def user_play_list(uid, offset=0, limit=1000):
    """获取用户歌单，包含收藏的歌单
    
    :param uid: 用户的ID，可通过登录或者其他接口获取
    :param offset: (optional) 分段起始位置，默认 0
    :param limit: (optional) 数据上限多少行，默认 1000
    """
    if uid is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'USER_PLAY_LIST'
    r.data = {'offset': offset, 'uid': uid, 'limit': limit, 'csrf_token': ''}
    r.send()
    return r.response


def user_dj(uid, offset=0, limit=30):
    """获取用户电台数据

    :param uid: 用户的ID，可通过登录或者其他接口获取
    :param offset: (optional) 分段起始位置，默认 0
    :param limit: (optional) 数据上限多少行，默认 30
    """
    if uid is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'USER_DJ'
    r.data = {'offset': offset, 'limit': limit, "csrf_token": ""}
    r.params = {'uid': uid}
    r.send()

    return r.response


def search(keyword, type=1, offset=0, limit=30):
    """搜索歌曲，支持搜索歌曲、歌手、专辑等

    :param keyword: 关键词
    :param type: (optional) 搜索类型，1: 单曲, 100: 歌手, 1000: 歌单, 1002: 用户
    :param offset: (optional) 分段起始位置，默认 0
    :param limit: (optional) 数据上限多少行，默认 30
    """
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
    """获取用户关注列表

    :param uid: 用户的ID，可通过登录或者其他接口获取
    :param offset: (optional) 分段起始位置，默认 0
    :param limit: (optional) 数据上限多少行，默认 30
    """
    if uid is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'USER_FOLLOWS'
    r.params = {'uid': uid}
    r.data = {'offset': offset, 'limit': limit, 'order': True}
    r.send()

    return r.response


def user_followeds(uid, offset='0', limit=30):
    """获取用户粉丝列表

    :param uid: 用户的ID，可通过登录或者其他接口获取
    :param offset: (optional) 分段起始位置，默认 0
    :param limit: (optional) 数据上限多少行，默认 30
    """
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
    """获取用户动态

    :param uid: 用户的ID，可通过登录或者其他接口获取
    """
    if uid is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'USER_EVENT'
    r.params = {'uid': uid}
    r.data = {'time': -1, 'getcounts': True, "csrf_token": ""}
    r.send()

    return r.response


def user_record(uid, type=0):
    """获取用户的播放列表,必须登录

    :param uid: 用户的ID，可通过登录或者其他接口获取
    :param type: (optional) 数据类型，0：获取所有记录，1：获取 weekData
    """
    if uid is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'USER_RECORD'
    r.data = {'type': type, 'uid': uid, "csrf_token": ""}
    r.send()

    return r.response


def event():
    """获取好友的动态，包括分享视频、音乐、动态等

    """
    r = NCloudBot()
    r.method = 'EVENT'
    r.data = {"csrf_token": ""}
    r.send()

    return r.response


# TOP_PLAYLIST_HIGHQUALITY
def top_playlist_highquality(cat='全部', offset=0, limit=20):
    """获取网易云音乐的精品歌单

    :param cat: (optional) 歌单类型，默认 ‘全部’，比如 华语、欧美等
    :param offset: (optional) 分段起始位置，默认 0
    :param limit: (optional) 数据上限多少行，默认 20
    """
    r = NCloudBot()
    r.method = 'TOP_PLAYLIST_HIGHQUALITY'
    r.data = {'cat': cat, 'offset': offset, 'limit': limit}
    r.send()

    return r.response


# PLAY_LIST_DETAIL
def play_list_detail(id, limit=20):
    """获取歌单中的所有音乐。由于获取精品中，只能看到歌单名字和 ID 并没有歌单的音乐，因此增加该接口传入歌单 ID
    获取歌单中的所有音乐.

    :param id: 歌单的ID
    :param limit: (optional) 数据上限多少行，默认 20
    """
    if id is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'PLAY_LIST_DETAIL'
    r.data = {'id': id, 'limit': limit, "csrf_token": ""}
    r.send()

    return r.response


# MUSIC_URL
def music_url(ids=[]):
    """通过歌曲 ID 获取歌曲下载地址

    :param ids: 歌曲 ID 的 list 
    """
    if not isinstance(ids, list):
        raise ParamsError()
    r = NCloudBot()
    r.method = 'MUSIC_URL'
    r.data = {'ids': ids, 'br': 999000, "csrf_token": ""}
    r.send()

    return r.response


# LYRIC
def lyric(id):
    """通过歌曲 ID 获取歌曲歌词地址

    :param id: 歌曲ID
    """
    if id is None:
        raise ParamsError()
    r = NCloudBot()
    r.method = 'LYRIC'
    r.params = {'id': id}
    r.send()

    return r.response


# MUSIC_COMMENT
def music_comment(id, offset=0, limit=20):
    """获取歌曲的评论列表

    :param id: 歌曲 ID
    :param offset: (optional) 分段起始位置，默认 0
    :param limit: (optional) 数据上限多少行，默认 20
    """
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
    """通过歌曲 ID 获取歌曲的详细信息

    :param ids: 歌曲 ID 的 list
    """
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
    """ 个人的 FM ,必须在登录之后调用，即 login 之后调用
    """
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