#!/usr/bin/env python
"""Timer classes with in-built summaries"""
import time
from typing import Any
from ..logger import Logger
logger = Logger(__name__)

class Timer():
    def __init__(self):
        self.times = {}
        self.names = {}

    def __call__(self, fn, *args, code: Any = None, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        end = time.perf_counter()
        self.times[code] = end - start
        self.names[code] = fn.__name__
        return result

    @property
    def total(self) -> float:
        return sum(list(self.times.values()))

    @property
    def summary(self) -> str:
        result = (
            f"Timing Summary ({self.total:.6f}s)\n"
            "----------------------------------\n"
            f"{'Code':<9}{'Name':<16}{'Time':<6}\n"
        )
        for key in self.times:
            result += (
                f"<{key:.>5}>  {self.names[key]:<15}"
                f" {self.times[key]:.6f}s\n"
            )
        result += "----------------------------------"
        return result