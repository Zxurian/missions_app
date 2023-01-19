from __future__ import annotations
import time


class Stopwatch:
    """Stopwatch class for tracking start & stop times

    This class will handle tracking time elapsed of desired actions based
    on the start & stop times. The start and stop times are immutable
    so stopwatch times will keep for the duration of the instance.

    ...

    """
    __start_time = None
    __stop_time = None
    __total_time = None

    def __int__(self, start_stopwatch=False) -> Stopwatch:
        """Initializes the class, optionally starting the stopwatch at the time time if True is provided

        @param start_stopwatch: bool (False)
        @return:
        """
        if start_stopwatch:
            self.__start_time = time.perf_counter()
        return self

    def start(self) -> Stopwatch:
        """Starts the stopwatch

        @return: Stopwatch
        """
        if self.__stop_time is not None:
            raise StopwatchException(StopwatchException.STOPWATCH_ALREADY_STOPPED)

        if self.__start_time is not None:
            raise StopwatchException(StopwatchException.STOPWATCH_ALREADY_STARTED)

        self.__start_time = time.perf_counter()
        return self

    def stop(self) -> Stopwatch:
        """

        @return:
        """
        if self.__start_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STARTED)

        if self.__stop_time is not None:
            raise StopwatchException(StopwatchException.STOPWATCH_ALREADY_STOPPED)

        self.__stop_time = time.perf_counter()
        self.__total_time = self.__stop_time - self.__start_time
        return self

    def get_total_time(self) -> float:
        """Get the total time difference between starting and stopping in seconds

        @return: float
        """
        if self.__start_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STARTED)
        if self.__stop_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STOPPED)

        return self.__total_time

    def get_elapsed(self) -> float:
        """Get the current time elapsed since the stopwatch was started, or the total time if already stopped

        @return: float
        """
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
