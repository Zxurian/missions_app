import time


class Stopwatch:
    start_time = None
    stop_time = None
    total_time = None

    def start(self) -> Stopwatch:
        self.start_time = time.perf_counter()
        return self

    def stop(self) -> Stopwatch:
        self.stop_time = time.perf_counter()
        self.total_time = self.stop_time - self.start_time
        return self

    def get_total_time(self) -> float:
        return self.total_time

    def get_elapsed(self) -> float:
        return time.perf_counter() - self.start_time

