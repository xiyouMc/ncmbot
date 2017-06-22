# coding:utf-8
import unittest
import ncmbot


class NCloudBotTestSuite(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        """Teardown."""
        pass

    # def test_USER_PLAY_LIST(self):
    #     # r = NCloudBot.user_play_list(uid='36554272')
    #     # print r.content
    #     pass

    def test_USER_DJ(self):
        r = ncmbot.user_dj(uid='36554272')
        print 'test_USER_DJ', r.content
        pass

    def test_SEARCH(self):
        r = ncmbot.search(keyword='Oh')
        print 'test_SEARCH', r.content
        pass

    def test_USER_FOLLOWS(self):
        r = ncmbot.user_follows(uid='36554272')
        print 'test_USER_FOLLOWS', r.content
        pass

    def test_USER_FOLLOWEDS(self):
        r = ncmbot.user_followeds(uid='36554272')
        print 'test_USER_FOLLOWEDS', r.content
        pass

    def test_USER_EVENT(self):
        r = ncmbot.user_event(uid='36554272')
        print 'test_USER_EVENT', r.content
        pass

    def test_USER_RECORD(self):
        ncmbot.login(phone='xxx', password='yyy')
        r = ncmbot.user_record(uid='264893698')
        print 'test_USER_RECORD', r.content
        pass

    def test_EVENT(self):
        ncmbot.login(phone='xxx', password='yyy')
        r = ncmbot.event()
        print 'test_EVENT', r.content
        pass

    def test_TOP_PLAYLIST_HIGHQUALITY(self):
        r = ncmbot.top_playlist_highquality()
        print 'test_TOP_PLAYLIST_HIGHQUALITY', r.content
        pass

    def test_PLAY_LIST_DETAIL(self):
        r = ncmbot.play_list_detail(id='326432061')
        print 'test_PLAY_LIST_DETAIL', r.content
        pass

    def test_LOGIN(self):
        r = ncmbot.login(phone='xxx', password='yyy')
        print 'test_LOGIN', r.content
        pass

    def test_MUSIC_URL(self):
        r = ncmbot.music_url(ids=[
            68302,
        ])
        print 'test_MUSIC_URL', r.content
        pass

    def test_LYRIC(self):
        r = ncmbot.lyric(id=68302)
        print 'test_LYRIC', r.content
        pass

    def test_MUSIC_COMMENT(self):
        r = ncmbot.music_comment(id=68302)
        print 'test_MUSIC_COMMENT', r.content

    # def test_ALBUM_COMMENT(self):
    #     r = ncmbot.album_comment(id=)

    def test_SONG_DETAIL(self):
        r = ncmbot.song_detail([
            68302,
            30500857,
        ])
        print 'test_SONG_DETAIL', r.json()

    def test_PERSONAL_FM(self):
        ncmbot.login(phone='xxx', password='yyy')
        r = ncmbot.personal_fm()
        print 'test_PERSONAL_FM', r.content


if __name__ == '__main__':
    unittest.main()