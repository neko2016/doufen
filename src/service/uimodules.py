# encoding: utf-8
import tornado
import db

class Account(tornado.web.UIModule):
    """
    登录帐号模块
    """

    def render(self):
        try:
            account = db.Account.getDefault()
        except db.Account.DoesNotExist:
            account = None
        return self.render_string('modules/account.html', account=account)


class Movie(tornado.web.UIModule):
    """
    电影卡片
    """

    def render(self, douban_id):
        try:
            movie = db.Movie.get(db.Movie.douban_id == douban_id)
        except db.Movie.DoesNotExist:
            movie = None
        return self.render_string('modules/movie.html', movie=movie)



class Book(tornado.web.UIModule):
    """
    图书卡片
    """

    def render(self, douban_id):
        try:
            book = db.Book.get(db.Book.douban_id == douban_id)
        except db.Book.DoesNotExist:
            book = None
        return self.render_string('modules/book.html', book=book)


class Music(tornado.web.UIModule):
    """
    音乐卡片
    """

    def render(self, douban_id):
        try:
            music = db.Music.get(db.Music.douban_id == douban_id)
        except db.Music.DoesNotExist:
            music = None
        return self.render_string('modules/music.html', music=music)
