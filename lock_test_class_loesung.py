from threading import RLock,Thread
from time import sleep
from logging import debug,DEBUG,basicConfig
from random import randint

basicConfig(level=DEBUG,
            format='(%(threadName)-9s) %(asctime)-15s %(message)s')
                    
class Counter(object):
    def __init__(self, start = 0):
        self.lock = RLock()
        self.value = start
    def increment(self):
        debug('Waiting for a lock')
        self.lock.acquire()
        try:
            debug('Acquired a lock - sleep 5 s')
            sleep(5)
            self.value = self.value + 1
            debug("New value:"+str(self.value))
        finally:
            debug('Released a lock')
            self.lock.release()

def worker(c):
    r = randint(1,10)
    debug('Sleeping %0.02f', r)
    sleep(r)
    c.increment()

if __name__ == '__main__':
    counter = Counter(17)
    for i in range(2):
        t = Thread(target=worker, args=(counter,))
        t.start()

