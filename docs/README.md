# NCloudBot

> 这是一个网易云音乐的 Python 组件库，你可以随心所欲的玩音乐。
## 感谢

- 感谢 [darknessomi](https://github.com/darknessomi/musicbox) 为本组件提供算法支持

## 简介
NCloudBot 给你提供了多种接口，你可以登录、获取动态、获取音乐列表、下载音乐等等的。旨在将网易云音乐的接口封装为组件，提供给开发者在任何平台使用。

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

## 安装
```shell
$ pip install NCloudBot
or
$ easy_install NCloudBot
```

## 接口文档
- 其中登录等部分接口不能调用太频繁，否则会出现 ip 高频错误，若需要高频调用，可以增加 IP 代理池
- 本项目旨在学习，同时将组件提供出来，开发者可以在项目中依赖使用。

### 登录
登录接口支持手机号、邮箱

**参数解释**

|参数名|可选|简介|
|----|----|----|
|phone|可选（和 email 二选一）|账号为手机号
|email|可选（和 phone 二选一）| 账号为邮箱
|password|必选|密码

**接口**

`NCloudBot.login`

**调用例子**

`NCloudBot.login(phone='xxx', password='yyy')`

**返回处理**

```python
bot = NCloudBot.login(phone='xxx', password='yyy')
bot.content # bot.json()
```

### 获取用户歌单
获取用户的歌单，包含收藏的歌单。不需要登录。


**参数解释**

|参数名|可选|简介|
|----|----|----|
|uid|必选|用户的ID，ID可以通过登录、或者其他接口获取
|offset|可选，默认0| 分段处理，开始位置
|limit| 可选，默认1000 |最多获取多少行数据

**接口**

`NCloudBot.user_play_list`

**调用例子**

`NCloudBot.user_play_list(uid='36554272')`

### 获取用户电台
获取用户的 FM 电台歌曲列表。无需登录


**参数解释**

|参数名|可选|简介|
|----|----|----|
|uid|必选|用户的ID，ID可以通过登录、或者其他接口获取
|offset|可选，默认0| 分段处理，开始位置
|limit| 可选，默认30 |最多获取多少行数据

**接口**

`NCloudBot.user_dj`

**调用例子**

`NCloudBot.user_dj(uid='36554272')`

### 获取用户关注列表
获取用户的关注列表。无需登录

**参数解释**

|参数名|可选|简介|
|----|----|----|
|uid|必选|用户的ID，ID可以通过登录、或者其他接口获取
|offset|可选，默认0| 分段处理，开始位置
|limit| 可选，默认30 |最多获取多少行数据

**接口**

` NCloudBot.user_follows`

**调用例子**

` NCloudBot.user_follows(uid='36554272')`

### 获取用户粉丝
获取用户的粉丝列表。无需登录

**参数解释**

|参数名|可选|简介|
|----|----|----|
|uid|必选|用户的ID，ID可以通过登录、或者其他接口获取
|offset|可选，默认0| 分段处理，开始位置
|limit| 可选，默认30 |最多获取多少行数据

**接口**

` NCloudBot.user_followeds`

**调用例子**

` NCloudBot.user_followeds(uid='36554272')`

### 获取用户动态
获取用户的动态。无需登录

**参数解释**

|参数名|可选|简介|
|----|----|----|
|uid|必选|用户的ID，ID可以通过登录、或者其他接口获取


**接口**

` NCloudBot.user_event`

**调用例子**

` NCloudBot.user_event(uid='36554272')`

### 获取用户播放列表
获取用户的播放列表。无需登录。

**参数解释**

|参数名|可选|简介|
|----|----|----|
|uid|必选|用户的ID，ID可以通过登录、或者其他接口获取
|type|可选，默认 0| 0:获取所有数据 allData 1：获取 weekData


**接口**

`NCloudBot.user_record`

**调用例子**

`NCloudBot.user_record(uid='36554272')`


### 获取好友的动态
需要登录。获取用户界面的所有动态，包括分享视频、音乐、动态等等的。


**接口**

`NCloudBot.event()`

**调用例子**

```python
NCloudBot.login(phone='18291994584', password='cxdcxd')
bot = NCloudBot.event()
print bot.content
```


### 获取精品歌单
获取网易云音乐的精品歌单。无需登录。

**参数解释**

|参数名|可选|简介|
|----|----|----|
|cat|可选，默认 ‘全部’|歌单的类别，比如 华语、欧美等
|offset|可选，默认0| 分段处理，开始位置
|limit| 可选，默认20 |最多获取多少行数据



**接口**

`NCloudBot.top_playlist_highquality`

**调用例子**

`NCloudBot.top_playlist_highquality(cat='华语')`


### 获取歌单中的所有音乐
由于获取精品歌单，只能看到歌单名字不能拿到歌单中的音乐，因此增加该接口传入歌单ID，获取歌单中的所有音乐.

无需登录

**参数解释**

|参数名|可选|简介|
|----|----|----|
|id|必选|从精品歌单接口中获取到的ID
|limit| 可选，默认20 |最多获取多少行数据



**接口**

`NCloudBot.play_list_detail`

**调用例子**

`NCloudBot.play_list_detail(id='326432061')`



### 获取音乐的下载地址
通过指定音乐的 ID 来获取该音乐的下载地址。其中 ID 可传入数组。

无需登录

**参数解释**

|参数名|可选|简介|
|----|----|----|
|ids|必选|音乐的 ID 数组



**接口**

`NCloudBot.music_url`

**调用例子**

```python
r = NCloudBot.music_url(ids=[68302,])
print r.content
```

### 搜索
可通过歌曲、歌手、专辑等关键字搜索歌曲列表

无需登录

**参数解释**

|参数名|可选|简介|
|----|----|----|
|keywords|必选|关键字
|type|可选，默认 1|  1：单曲 、100：歌手、1000：歌单、1002：用户
|offset|可选，默认0| 分段处理，开始位置
|limit| 可选，默认30 |最多获取多少行数据


**接口**

`NCloudBot.search`

**调用例子**

```python
NCloudBot.search(keyword='东风破')
```

### 获取歌词
通过歌曲 ID 获取与之对应的歌词

无需登录

**参数解释**

|参数名|可选|简介|
|----|----|----|
|id|必选|歌曲ID

**接口**

`NCloudBot.lyric`

**调用例子**

```python
NCloudBot.lyric(id = 68302)
```

### 获取音乐的评论
通过歌曲 ID 获取该歌曲的评论

无需登录

**参数解释**

|参数名|可选|简介|
|----|----|----|
|id|必选|歌曲ID


**接口**

`NCloudBot.music_comment`

**调用例子**

```python
NCloudBot.music_comment(id=68302)
```

### 获取歌曲详情
通过歌曲 ID 获取该歌曲的详情，并支持数组

无需登录

**参数解释**

|参数名|可选|简介|
|----|----|----|
|ids|必选|歌曲 ID 的 list


**接口**

`NCloudBot.song_detail`

**调用例子**

```python
r = NCloudBot.song_detail([
            68302,
            30500857,
        ])
print r.content
```

### 获取私人 FM
通过歌曲 ID 获取该歌曲的详情，并支持数组

必须登录

**参数解释**

|参数名|可选|简介|
|----|----|----|
|ids|必选|歌曲 ID 的 list


**接口**

`NCloudBot.personal_fm`

**调用例子**

```python
NCloudBot.personal_fm()```