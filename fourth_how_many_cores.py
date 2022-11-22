from multiprocessing import Process
from datetime import datetime, timedelta
import time


def task():
    time.sleep(1)


# 4.1
def main():
    times = []
    n = 36

    for i in range(1, n + 1):

        processes = []

        for j in range(i):
            p = Process(target=task)
            processes.append(p)

        start_time = datetime.now()

        for p in processes:
            p.start()

        for p in processes:
            p.join()

        end_time = datetime.now()

        dt = end_time - start_time
        t = dt / timedelta(microseconds=1)
        times.append(t)

        print(f"{i} done.")

    return times


if __name__ == "__main__":
    data = main()

    from matplotlib import pyplot as plt

    plt.plot(range(1, len(data) + 1), data)
    plt.show()
