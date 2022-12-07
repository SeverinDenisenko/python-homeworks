from multiprocessing import Pool, set_start_method


def task(magic):
    s = 1
    for i in range(len(magic)):
        s *= ord(magic[i])


def cal_task(magic):
    pass
    # magic help please


# 4.1
def test():
    from datetime import datetime, timedelta

    times = []
    n = 16
    passes = 500000

    set_start_method("spawn")

    Pool(1).map(task, "magic" * passes * 1)

    for i in range(1, n + 1):
        # Find out how much takes to copy processes

        start_time = datetime.now()

        with Pool(i) as p:
            p.map(cal_task, "magic" * passes * i)

        end_time = datetime.now()

        dt_cal = end_time - start_time
        t_cal = dt_cal / timedelta(seconds=1)

        # Find out how much takes to run processes

        start_time = datetime.now()

        with Pool(i) as p:
            p.map(task, "magic" * passes * i)

        end_time = datetime.now()

        dt = end_time - start_time
        t = dt / timedelta(seconds=1)

        # Put in results

        times.append(t - t_cal)

        print(f"{i} done.")

    return times


def main():
    data = test()
    estimate = 0
    very_magic_number = 0.7

    for i in range(len(data)):
        data[i] /= data[0]

        if data[i] < very_magic_number:
            estimate += 1

    from matplotlib import pyplot as plt

    print(f"Estimated number of cores: {estimate}")

    plt.plot(range(1, len(data) + 1), data)
    plt.show()


if __name__ == "__main__":
    main()
