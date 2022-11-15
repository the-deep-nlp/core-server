import time


class log_time:
    def __init__(self, block_name='BLOCK'):
        self.block_name = block_name
        self.start = 0
        self.end = 0

    def __enter__(self, *args, **kwargs):
        self.start = time.time()

    def log(self):
        dtime = self.end - self.start
        print(f'{self.block_name} took {round(dtime, 4)} seconds.')

    def __exit__(self, *args, **kwargs):
        self.end = time.time()
        self.log()

    def __call__(self, f):
        self.block_name = f.__name__

        def wrapped_f(*args, **kwargs):
            self.start = time.time()
            res = f(*args, **kwargs)
            self.end = time.time()
            self.log()
            return res
        return wrapped_f
