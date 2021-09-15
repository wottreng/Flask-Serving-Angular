from datetime import timedelta
class Config(object):
    SECRET_KEY = 'secret!!'
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    REMEMBER_COOKIE_DURATION = timedelta(days=7)
    REMEMBER_COOKIE_NAME = "cookieMonster"
    REMEMBER_COOKIE_SECURE = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_REFRESH_EACH_REQUEST = False
    REMEMBER_COOKIE_PATH = "/"
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_NAME = "cookieTime"
    SESSION_COOKIE_SAMESITE = "Lax"
    SEND_FILE_MAX_AGE_DEFAULT = timedelta(seconds=43200)