"""
Container for the Runner class
"""
import functools
from typing import Iterable, Union, Callable

class Runner:
    """Subclass the Runner class to create a customisable
    runner, akin to those found in continuous integration systems

    >>> class MyRunner(Runner):
    >>>     def __init__(self):
    >>>         super().__init__()
    """
    __tasks__ = {}
    
    def add_task(self, code: int, function: Callable):
        """Adds a function to the list of tasks

        Params:
            code: ID of the task
            function: thing to call during `Runner.execute`
        """
        self.__tasks__[code] = function

    @classmethod
    def task(cls, code: int):
        """Decorate a method with `@Runner.task(code: int)` to allocate it
        to the list of tasks to run. Use the code to chose the order 
        which occurs in ascending values

        Parameters:
            code: ID of the task
        """
        def outer(func):
            cls.add_task(cls, code, func)
            @functools.wraps(func)
            def wrapper(cls, *args, **kwargs):
                return func(cls, *args, **kwargs)
            return wrapper
        return outer

    def execute(self, skip: Union[int, Iterable, None] = None):
        """Run all of the tasks in order, which is determined by their code

        Parameters:
            skip: codes to skip
        """
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
                