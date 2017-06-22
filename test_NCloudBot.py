# coding:utf-8
import NCloudBot
import unittest


class NCloudBotTestSuite(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        """Teardown."""
        pass

    def test_USER_PLAY_LIST(self):
        # r = NCloudBot.user_play_list(uid='36554272')
        # print r.content
        pass

    def test_USER_DJ(self):
        r = NCloudBot.user_dj(uid='36554272')
        print r.content
        pass

    def test_SEARCH(self):
        # r = NCloudBot.search(keyword='Oh')
        # print r.content
        pass

    def test_USER_FOLLOWS(self):
        r = NCloudBot.user_follows(uid='36554272')
        print r.content
        pass

    def test_USER_FOLLOWEDS(self):
        # r = NCloudBot.user_followeds(uid='36554272')
        # print r.content
        pass

    def test_USER_EVENT(self):
        # r = NCloudBot.user_event(uid='36554272')
        # print r.content
        pass

    def test_USER_RECORD(self):
        # r = NCloudBot.user_record(uid='36554272')
        # print r.content
        pass

    def test_EVENT(self):
        # l = NCloudBot.login(phone='18291994584', password='cxdcxd')
        # r = NCloudBot.event()
        # print r.content
        pass

    def test_TOP_PLAYLIST_HIGHQUALITY(self):
        # r = NCloudBot.top_playlist_highquality()
        # print r.content
        pass

    def test_PLAY_LIST_DETAIL(self):
        # r = NCloudBot.play_list_detail(id='326432061')
        # print r.content
        pass

    def test_LOGIN(self):
        # r = NCloudBot.login(phone='18291994584', password='cxdcxd')
        # print r.status_code
        pass

    def test_MUSIC_URL(self):
        # r = NCloudBot.music_url(ids=[
        #     68302,
        # ])
        # print r.content
        pass

    def test_LYRIC(self):
        # r = NCloudBot.lyric(id = 68302)
        # print 'test_LYRIC',r.content
        pass

    def test_MUSIC_COMMENT(self):
        r = NCloudBot.music_comment(id=68302)
        # print 'test_MUSIC_COMMENT', r.content

    # def test_ALBUM_COMMENT(self):
    #     r = NCloudBot.album_comment(id=)
    def test_SONG_DETAIL(self):
        r = NCloudBot.song_detail([
            68302,
            30500857,
        ])
        print r.content
    
    def test_PERSONAL_FM(self):
        NCloudBot.login(phone='18291994584', password='cxdcxd')
        r = NCloudBot.personal_fm()
        print r.content


if __name__ == '__main__':
    unittest.main()