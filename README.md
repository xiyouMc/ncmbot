![][py2x] ![][rating] ![][build] [![GitHub license][license]][license_file]

NeteaseCloud Bot for Philharmonic™
===========

[文档说明](http://xiyoumc.0x2048.com/ncbot/#/)

## 简介
* `ncbot` 是 NeteaseCloudBot (网易云音乐助手) 的简称
* `ncbot` 是一个 Python 的第三方组件
* 实现了 网易云音乐 的 API 封装
* 提供了轻量化的接口，高效的扩充音乐库
* 同时，提供了私人 FM 等接口，你可以通过分析准确的找到自己喜欢的音乐

## 环境、架构

开发语言： Python2.x

开发环境： MacOS系统、4G内存

* 主要使用了 Requests 开源库
* 基于网易云音乐 API 的定义，完成 Python 组件的封装
* 轻量化的接口设计

## 安装

* pip install ncbot
* easy_install ncbot

## 接口列表
1. 登录
2. 获取用户歌单
3. 获取用户电台
4. 获取用户关注列表
5. 获取用户粉丝
6. 获取用户动态
7. 获取用户播放列表
8. 获取好友的动态
9. 获取精品歌单
10. 获取歌单中的所有音乐
11. 获取音乐的下载地址
12. 搜索
13. 获取歌词
14. 获取音乐的评论
15. 获取歌曲详情
16. 获取私人 FM
17. ...

## 使用

```python
import ncbot
bot = ncbot.login(phone='xxx', password='yyy')
bot.content # bot.json()
```
![](https://github.com/xiyouMc/ncbot/blob/master/image/login.png?raw=true)

## 联系我

* 关注微信公众号: DeveloperPython

<img src="https://github.com/xiyouMc/ncbot/blob/master/image/qrcode.jpg?raw=true" width = "200" height = "200" alt="图片名称" align=center />   


[build]: https://img.shields.io/badge/build-passing-brightgreen.svg
[rating]: https://img.shields.io/badge/rating-4.7%2F5-brightgreen.svg
[license_file]: https://raw.githubusercontent.com/xiyouMc/ncbot/master/LICENSE
[license]: https://img.shields.io/badge/license-ISC-blue.svg
[stars]: https://img.shields.io/github/stars/xiyouMc/ncbot.svg
[stargazers]: https://github.com/xiyouMc/ncbot/stargazers
[fork]: https://img.shields.io/github/forks/xiyouMc/ncbot.svg
[network]: https://github.com/xiyouMc/ncbot/network

[py2x]: https://img.shields.io/badge/python-2.x-brightgreen.svg

[issues_img]: https://img.shields.io/github/issues/xiyouMc/ncbot.svg
[issues]: https://github.com/xiyouMc/ncbot/issues