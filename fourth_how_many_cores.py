from multiprocessing import Pool
from datetime import datetime, timedelta
import time


def task(magic):
    time.sleep(1)
    # magic help please


def cal_task(magic):
    time.sleep(0.000001)
    # magic help please


# 4.1
def test():
    times = []
    cal_times = []
    n = 16

    for i in range(1, n + 1):
        start_time = datetime.now()

        with Pool(i) as p:
            p.map(cal_task, ["magic"] * i)

        end_time = datetime.now()

        dt = end_time - start_time
        t = dt / timedelta(seconds=1)
        cal_times.append(t)

    for i in range(1, n + 1):
        start_time = datetime.now()

        with Pool(i) as p:
            p.map(task, ["magic"] * i)

        end_time = datetime.now()

        dt = end_time - start_time
        t = dt / timedelta(seconds=1)
        times.append(t)

        print(f"{i} done.")

    for i in range(n):
        times[i] -= cal_times[i]

    return times


def main():
    data = test()
    estimate1 = 0
    estimate2 = 0

    for t in data:
        if t < 1.08:
            estimate1 += 1

    for t in data:
        if t < 1.1:
            estimate2 += 1

    print(f"Number of cores: {estimate2} - {estimate1}")

    from matplotlib import pyplot as plt

    plt.plot(range(1, len(data) + 1), data)
    plt.show()


if __name__ == "__main__":
    main()
