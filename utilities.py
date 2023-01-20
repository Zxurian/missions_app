from __future__ import annotations
import time


class Stopwatch:
    """Stopwatch class for tracking start & stop times relative to program start

    This class will handle tracking time elapsed of desired actions based
    on the start & stop times. The start and stop times are immutable
    so stopwatch times will keep for the duration of the instance.
    """

    __start_time = None
    __stop_time = None
    __total_time = None

    def __init__(self, start_stopwatch=False) -> None:
        """Initialize the Stopwatch, optionally starting it at the same time

        :param start_stopwatch: bool
        :return: Stopwatch
        """
        if start_stopwatch:
            self.start()

    def start(self) -> Stopwatch:
        """Start the stopwatch

        :return: Stopwatch
        """
        if self.__stop_time is not None:
            raise StopwatchException(StopwatchException.STOPWATCH_ALREADY_STOPPED)

        if self.__start_time is not None:
            raise StopwatchException(StopwatchException.STOPWATCH_ALREADY_STARTED)

        self.__start_time = time.perf_counter()
        return self

    def get_start(self) -> float:
        """Get the start time of the stopwatch

        :return: float
        """
        if self.__start_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STARTED)

        return self.__start_time

    def stop(self) -> Stopwatch:
        """Stop the stopwatch

        :return: Stopwatch
        """
        if self.__start_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STARTED)

        if self.__stop_time is not None:
            raise StopwatchException(StopwatchException.STOPWATCH_ALREADY_STOPPED)

        self.__stop_time = time.perf_counter()
        self.__total_time = self.__stop_time - self.__start_time
        return self

    def get_stop(self) -> float:
        """Get the stop time of the stopwatch

        :return: float
        """
        if self.__start_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STARTED)

        if self.__stop_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STOPPED)

        return self.__stop_time

    def get_total_time(self) -> float:
        """Get the delta difference between start and stopped in seconds

        :return: float
        """
        if self.__start_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STARTED)
        if self.__stop_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STOPPED)

        return self.__total_time

    def get_elapsed(self) -> float:
        """Get the delta since the start of the stopwatch in seconds. Returns total time if stopped.

        :return:
        """
        if self.__start_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STARTED)

        if self.__stop_time is None:
            return time.perf_counter() - self.__start_time
        else:
            return self.__total_time


class StopwatchException(Exception):
    """Exception Class for the Stopwatch Class"""

    STOPWATCH_NOT_STARTED = 'Stopwatch is not started yet'
    STOPWATCH_ALREADY_STARTED = 'Stopwatch is already started'
    STOPWATCH_NOT_STOPPED = 'Stopwatch is not stopped yet'
    STOPWATCH_ALREADY_STOPPED = 'Stopwatch is already stopped'
