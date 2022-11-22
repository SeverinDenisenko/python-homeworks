from queue import Queue
from threading import Thread
from numpy import random
from time import sleep
import math


class Receiver:
    def __init__(self, queue, sender):
        self.queue = queue
        self.sender = sender

    def start(self):
        Thread(target=self.__receiver__).start()

    def __receiver__(self):
        while True:
            data = self.queue.get()
            print(math.sin(data))
            if self.sender.is_ended:
                break


class Sender:
    def __init__(self, queue, n):
        self.queue = queue
        self.n = n
        self.is_ended = False

    def start(self):
        Thread(target=self.__sender__).start()

    def __sender__(self):
        data = random.rand(self.n)

        max_sleep_time = 2
        intervals = random.rand(self.n) * max_sleep_time

        for i in range(self.n):
            sleep(intervals[i])
            self.queue.put(data[i])

        self.is_ended = True


def main():
    queue = Queue()
    sender = Sender(queue, 3)
    receiver = Receiver(queue, sender)

    sender.start()
    receiver.start()


if __name__ == "__main__":
    main()
