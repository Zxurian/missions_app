from __future__ import annotations
import time


class Stopwatch:
    start_time = None
    stop_time = None
    total_time = None

    def start(self) -> Stopwatch:
        if self.stop_time is not None:
            raise StopwatchException(StopwatchException.STOPWATCH_ALREADY_STOPPED)

        if self.start_time is not None:
            raise StopwatchException(StopwatchException.STOPWATCH_ALREADY_STARTED)

        self.start_time = time.perf_counter()
        return self

    def stop(self) -> Stopwatch:
        if self.start_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STARTED)

        if self.stop_time is not None:
            raise StopwatchException(StopwatchException.STOPWATCH_ALREADY_STOPPED)

        self.stop_time = time.perf_counter()
        self.total_time = self.stop_time - self.start_time
        return self

    def get_total_time(self) -> float:
        if self.start_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STARTED)
        if self.stop_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STOPPED)

        return self.total_time

    def get_elapsed(self) -> float:
        if self.start_time is None:
            raise StopwatchException(StopwatchException.STOPWATCH_NOT_STARTED)

        if self.stop_time is None:
            return time.perf_counter() - self.start_time
        else:
            return self.total_time


class StopwatchException(Exception):
    STOPWATCH_NOT_STARTED = 'Stopwatch is not started yet'
    STOPWATCH_ALREADY_STARTED = 'Stopwatch is already started'
    STOPWATCH_NOT_STOPPED = 'Stopwatch is not stopped yet'
    STOPWATCH_ALREADY_STOPPED = 'Stopwatch is already stopped'
