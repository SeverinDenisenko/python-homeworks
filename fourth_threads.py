from queue import Queue
from threading import Thread
from numpy import random
from time import sleep
import math


class Receiver:
    def __init__(self, queue):
        self.queue = queue

    def start(self):
        Thread(target=self.__receiver__).start()

    def __receiver__(self):
        senders = 0

        while True:
            data = self.queue.get()

            if data == "begin":
                senders += 1
                continue

            if data == "end":
                senders -= 1
                if senders == 0:
                    break
                continue

            print(math.sin(data))


class Sender:
    def __init__(self, queue, n):
        self.queue = queue
        self.n = n

    def start(self):
        Thread(target=self.__sender__).start()

    def __sender__(self):
        data = random.rand(self.n)

        max_sleep_time = 2
        intervals = random.rand(self.n) * max_sleep_time

        self.queue.put("begin")

        for i in range(self.n):
            sleep(intervals[i])
            self.queue.put(data[i])

        self.queue.put("end")


def main():
    queue = Queue()
    Sender(queue, 3).start()
    Sender(queue, 3).start()
    Sender(queue, 3).start()
    Sender(queue, 3).start()
    Sender(queue, 3).start()
    Sender(queue, 3).start()
    Sender(queue, 3).start()
    Sender(queue, 3).start()
    Sender(queue, 3).start()
    Sender(queue, 3).start()

    receiver = Receiver(queue)
    receiver.start()


if __name__ == "__main__":
    main()
