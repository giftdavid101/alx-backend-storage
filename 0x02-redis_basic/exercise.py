#!/usr/bin/env python3
"""  Redis excercise file"""

import uuid
from typing import Union


class Cache:
    """ Defines a Cache class to interact with Redis """

    def __init__(self):
        """initialization"""

        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """stores data in Redis with key"""

        random_key = str(uuid.uuid4())
        self._redis.set(random_key, data)
        return random_key
