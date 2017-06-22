# coding:utf-8
import unittest
import ncbot


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
        r = ncbot.user_dj(uid='36554272')
        print r.content
        pass

    def test_SEARCH(self):
        r = ncbot.search(keyword='Oh')
        print r.content
        pass

    def test_USER_FOLLOWS(self):
        r = ncbot.user_follows(uid='36554272')
        print r.content
        pass

    def test_USER_FOLLOWEDS(self):
        r = ncbot.user_followeds(uid='36554272')
        print r.content
        pass

    def test_USER_EVENT(self):
        r = ncbot.user_event(uid='36554272')
        print r.content
        pass

    def test_USER_RECORD(self):
        r = ncbot.user_record(uid='36554272')
        print r.content
        pass

    def test_EVENT(self):
        ncbot.login(phone='18291994584', password='cxdcxd')
        r = ncbot.event()
        print r.content
        pass

    def test_TOP_PLAYLIST_HIGHQUALITY(self):
        r = ncbot.top_playlist_highquality()
        print r.content
        pass

    def test_PLAY_LIST_DETAIL(self):
        r = ncbot.play_list_detail(id='326432061')
        print r.content
        pass

    def test_LOGIN(self):
        # r = ncbot.login(phone='18291994584', password='cxdcxd')
        # print r.status_code
        pass

    def test_MUSIC_URL(self):
        r = ncbot.music_url(ids=[
            68302,
        ])
        print r.content
        pass

    def test_LYRIC(self):
        r = ncbot.lyric(id=68302)
        print 'test_LYRIC', r.content
        pass

    def test_MUSIC_COMMENT(self):
        r = ncbot.music_comment(id=68302)
        print 'test_MUSIC_COMMENT', r.content

    # def test_ALBUM_COMMENT(self):
    #     r = ncbot.album_comment(id=)

    def test_SONG_DETAIL(self):
        r = ncbot.song_detail([
            68302,
            30500857,
        ])
        print r.json()

    def test_PERSONAL_FM(self):
        ncbot.login(phone='18291994584', password='cxdcxd')
        r = ncbot.personal_fm()
        print r.content


if __name__ == '__main__':
    unittest.main()