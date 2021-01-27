import functools
from typing import Iterable

class Runner:

    __tasks__ = {}
    
    def add_task(self, code, function):
        self.__tasks__[code] = function

    @classmethod
    def task(cls, code: int):
        def outer(func):
            cls.add_task(cls, code, func)
            @functools.wraps(func)
            def wrapper(cls, *args, **kwargs):
                return func(cls, *args, **kwargs)
            return wrapper
        return outer

    def execute(self, skip=None):
        if not skip:
            for task in self.__tasks__.values():
                task(self)
        else:
            if isinstance(skip, Iterable):
                for i, task in self.__tasks__.items():
                    if i in skip: continue
                    task(self)
            else:
                for i, task in self.__tasks__.items():
                    if i == skip: continue
                    task(self)
                