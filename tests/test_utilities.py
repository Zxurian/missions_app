import unittest
import utilities
import time


class TestStopwatchFunctions(unittest.TestCase):

    def test_init(self):
        stopwatch = utilities.Stopwatch()
        self.assertIsNone(stopwatch._Stopwatch__start_time)
        self.assertIsNone(stopwatch._Stopwatch__stop_time)
        self.assertIsNone(stopwatch._Stopwatch__total_time)
        self.assertIsInstance(stopwatch, utilities.Stopwatch)

        stopwatch = utilities.Stopwatch(True)
        self.assertIsNotNone(stopwatch._Stopwatch__start_time)
        self.assertIsNone(stopwatch._Stopwatch__stop_time)
        self.assertIsNone(stopwatch._Stopwatch__total_time)
        self.assertIsInstance(stopwatch, utilities.Stopwatch)

    def test_start(self):
        stopwatch = utilities.Stopwatch()
        stopwatch.start()
        self.assertIsNotNone(stopwatch._Stopwatch__start_time)

        stopwatch = utilities.Stopwatch()
        stopwatch._Stopwatch__stop_time = 1.2345
        with self.assertRaises(utilities.StopwatchException) as exc:
            stopwatch.start()
        self.assertEqual(str(exc.exception), utilities.StopwatchException.STOPWATCH_ALREADY_STOPPED)

        stopwatch = utilities.Stopwatch()
        stopwatch._Stopwatch__start_time = 1.2345
        with self.assertRaises(utilities.StopwatchException) as exc:
            stopwatch.start()
        self.assertEqual(str(exc.exception), utilities.StopwatchException.STOPWATCH_ALREADY_STARTED)

    def test_get_start(self):
        time_value = 1.2345
        stopwatch = utilities.Stopwatch()
        stopwatch._Stopwatch__start_time = time_value
        self.assertEqual(time_value, stopwatch.get_start())

        stopwatch = utilities.Stopwatch()
        stopwatch._Stopwatch__start_time = None
        with self.assertRaises(utilities.StopwatchException) as exc:
            stopwatch.get_start()
        self.assertEqual(str(exc.exception), utilities.StopwatchException.STOPWATCH_NOT_STARTED)

    def test_stop(self):
        stopwatch = utilities.Stopwatch()
        stopwatch._Stopwatch__start_time = 0.0001
        stopwatch.stop()
        self.assertIsNotNone(stopwatch._Stopwatch__stop_time)
        self.assertEqual(stopwatch._Stopwatch__stop_time - stopwatch._Stopwatch__start_time, stopwatch._Stopwatch__total_time)

        stopwatch = utilities.Stopwatch()
        stopwatch._Stopwatch__start_time = None
        with self.assertRaises(utilities.StopwatchException) as exc:
            stopwatch.stop()
        self.assertEqual(str(exc.exception), utilities.StopwatchException.STOPWATCH_NOT_STARTED)

        stopwatch = utilities.Stopwatch()
        stopwatch._Stopwatch__start_time = 1.2345
        stopwatch._Stopwatch__stop_time = 2.3456
        with self.assertRaises(utilities.StopwatchException) as exc:
            stopwatch.stop()
        self.assertEqual(str(exc.exception), utilities.StopwatchException.STOPWATCH_ALREADY_STOPPED)

    def test_get_stop(self):
        stop_time_value = 4.5678
        stopwatch = utilities.Stopwatch()
        stopwatch._Stopwatch__start_time = 3.4567
        stopwatch._Stopwatch__stop_time = stop_time_value
        self.assertEqual(stop_time_value, stopwatch.get_stop())

        stopwatch = utilities.Stopwatch()
        stopwatch._Stopwatch__start_time = None
        with self.assertRaises(utilities.StopwatchException) as exc:
            stopwatch.get_stop()
        self.assertEqual(str(exc.exception), utilities.StopwatchException.STOPWATCH_NOT_STARTED)

        stopwatch = utilities.Stopwatch()
        stopwatch._Stopwatch__start_time = 1.2345
        stopwatch._Stopwatch__stop_time = None
        with self.assertRaises(utilities.StopwatchException) as exc:
            stopwatch.get_stop()
        self.assertEqual(str(exc.exception), utilities.StopwatchException.STOPWATCH_NOT_STOPPED)

    def test_get_total_time(self):
        total_time_value = 1.1101
        stopwatch = utilities.Stopwatch()
        stopwatch._Stopwatch__start_time = 5.6789
        stopwatch._Stopwatch__stop_time = 6.7890
        stopwatch._Stopwatch__total_time = total_time_value
        self.assertEqual(total_time_value, stopwatch.get_total_time())

        stopwatch = utilities.Stopwatch()
        stopwatch._Stopwatch__start_time = None
        with self.assertRaises(utilities.StopwatchException) as exc:
            stopwatch.get_total_time()
        self.assertEqual(str(exc.exception), utilities.StopwatchException.STOPWATCH_NOT_STARTED)

        stopwatch = utilities.Stopwatch()
        stopwatch._Stopwatch__start_time = 5.6789
        stopwatch._Stopwatch__stop_time = None
        with self.assertRaises(utilities.StopwatchException) as exc:
            stopwatch.get_total_time()
        self.assertEqual(str(exc.exception), utilities.StopwatchException.STOPWATCH_NOT_STOPPED)

    def test_get_elapsed(self):
        stopwatch = utilities.Stopwatch()
        stopwatch._Stopwatch__start_time = 0.00001
        self.assertIsNotNone(stopwatch.get_elapsed())

        total_time_value = 0.00005
        stopwatch._Stopwatch__stop_time = 0.00006
        stopwatch._Stopwatch__total_time = total_time_value
        self.assertEqual(total_time_value, stopwatch.get_elapsed())

        stopwatch = utilities.Stopwatch()
        stopwatch._Stopwatch__start_time = None
        with self.assertRaises(utilities.StopwatchException) as exc:
            stopwatch.get_elapsed()
        self.assertEqual(str(exc.exception), utilities.StopwatchException.STOPWATCH_NOT_STARTED)
