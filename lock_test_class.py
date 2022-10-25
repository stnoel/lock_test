from threading import Thread
from time import sleep
from logging import debug,DEBUG,basicConfig
from random import randint

basicConfig(level=DEBUG,
            format='(%(threadName)-9s) %(message)s')
                    
class Counter(object):
    def __init__(self, start = 0):
        self.value = start
    def increment(self):
        sleep(5)
        self.value = self.value + 1
        print("New value:",self.value)

def worker(c):
    r = randint(1,10)
    debug('Sleeping %0.02f', r)
    sleep(r)
    c.increment()

if __name__ == '__main__':
    counter = Counter()
    for i in range(2):
        t = Thread(target=worker, args=(counter,))
        t.start()

