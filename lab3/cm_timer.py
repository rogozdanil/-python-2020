import time
from contextlib import contextmanager


class cm_timer_1:

    def __init__(self):
        self.before_time = 0
        self.after_time = 0

    def __enter__(self):
        self.before_time = time.perf_counter()
        return time.perf_counter()

    def __exit__(self, exp_type, exp_value, traceback):
        self.after_time = time.perf_counter()
        print('time: {}'.format(round(self.after_time - self.before_time, 5)))


@contextmanager
def cm_timer_2():
    before_time = time.perf_counter()
    yield time.perf_counter()
    print('time: {}'.format(round(time.perf_counter() - before_time, 5)))


if __name__ == '__main__':
    with cm_timer_1():
        time.sleep(5.5)
    print('\n')

    with cm_timer_2():
        time.sleep(5.5)