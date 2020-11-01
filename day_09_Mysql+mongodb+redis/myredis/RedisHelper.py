from redis import *


class RedisHelper(object):
    def __init__(self, host, port, password):
        self.__redis = StrictRedis(host=host, port=port, password=password)

    def set(self, key, value):
        self.__redis.set(key, value)

    def get(self, key):
        return self.__redis.get(key)
