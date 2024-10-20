from threading import Lock
# from threading import Semaphore

class FooBar:
    def __init__(self, n):
        self.n = n
        self.foo_lock = Lock()
        self.bar_lock = Lock()
        self.bar_lock.acquire()
        # self.foo_gate = Semaphore(1)
        # self.bar_gate = Semaphore(0)

    def foo(self, printFoo: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            # same methods for semaphore and lock, with the increment/decrement diff
            self.foo_lock.acquire() 
            # printFoo() outputs "foo". Do not change or remove this line.
            printFoo()
            self.bar_lock.release()
                


    def bar(self, printBar: 'Callable[[], None]') -> None:
        
        for i in range(self.n):
            self.bar_lock.acquire()
            # printBar() outputs "bar". Do not change or remove this line.
            printBar()
            self.foo_lock.release()
            