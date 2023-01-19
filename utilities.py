from __future__ import annotations
import time

"""Stopwatch class for handling duration of actions

This class will handle tracking time elapsed of desired actions based
on the start & stop times. The start and stop times are immutable
so stopwatch times will keep for the duration of the instance.
"""
class Stopwatch:
    __start_time = None
    __stop_time = None
    __total_time = None

    def __int__(self, start_stopwatch=False) -> Stopwatch:
        if start_stopwatch:
            self.__start_time = time.perf_counter()
        return self

    def start(self) -> Stopwatch:
        if self.__stop_time is not None:
            raise StopwatchException(StopwatchException.STOPWATCH_ALREADY_STOPPED)

        if self.__start_time is not None:
            raise StopwatchException(StopwatchException.STOPWATCH_ALREADY_STARTED)

        self.__start_time = time.perf_counter()
        return self

    def stop(self) -> Stopwatch:
        if self.__start_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STARTED)

        if self.__stop_time is not None:
            raise StopwatchException(StopwatchException.STOPWATCH_ALREADY_STOPPED)

        self.__stop_time = time.perf_counter()
        self.__total_time = self.__stop_time - self.__start_time
        return self

    def get_total_time(self) -> float:
        if self.__start_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STARTED)
        if self.__stop_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STOPPED)

        return self.__total_time

    def get_elapsed(self) -> float:
        if self.__start_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STARTED)

        if self.__stop_time is None:
            return time.perf_counter() - self.__start_time
        else:
            return self.__total_time


class StopwatchException(Exception):
    STOPWATCH_NOT_STARTED = 'Stopwatch is not started yet'
    STOPWATCH_ALREADY_STARTED = 'Stopwatch is already started'
    STOPWATCH_NOT_STOPPED = 'Stopwatch is not stopped yet'
    STOPWATCH_ALREADY_STOPPED = 'Stopwatch is already stopped'
