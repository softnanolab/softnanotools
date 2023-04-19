"""Container for the Runner class."""
import functools
from typing import Any, Iterable, Callable

from ..timer import Timer
from ..logger import Logger

logger = Logger(__name__)


class Runner:
    """Subclass the Runner class to create a customisable
    runner, akin to those found in continuous integration systems.

    >>> class MyRunner(Runner):
    >>>     def __init__(self):
    >>>         super().__init__()
    """

    __tasks__ = {}

    def add_task(self, code: int, function: Callable):
        """Adds a function to the list of tasks.

        Params:
            code: ID of the task
            function: thing to call during `Runner.execute`
        """
        self.__tasks__[code] = function

    @classmethod
    def task(cls, code: int):
        """Allocate to the list of tasks to run.

        Decorate a method with `@Runner.task(code: int)` to use the code to
        choose the order which occurs in ascending values.

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

    def execute(self, skip: Iterable[Any] = None, time: bool = False):
        """Execute the Runner by iterating over all tasks and calling
        them.

        Arguments:
            skip:
                either the code or a list of codes to skip
            time:
                set to True for a timed summary
        """
        # initialise Timer object (or fake proxy)
        def proxy(fn, *args, code: int = -1, **kwargs):
            return fn(*args, **kwargs)

        if time:
            timer = Timer()
        else:
            timer = proxy

        # run a non-wrapped version of the tasks for simplicity
        if not skip and not time:
            for task in self.__tasks__.values():
                task(self)

        # otherwise parse the skips or the timer
        else:

            # if skipping is true
            if isinstance(skip, Iterable):
                for i, task in self.__tasks__.items():
                    if i in skip:
                        continue
                    timer(i, task, self)

            # otherwise just the timer
            else:
                for i, task in self.__tasks__.items():
                    if i == skip:
                        continue
                    timer(task, self, code=i)

        if time:
            logger.info(timer.summary)
