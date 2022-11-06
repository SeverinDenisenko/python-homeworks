import shelve
import random


# 3.9
def main():
    rnd = random.sample(range(0, 100), 100)

    with shelve.open("rnd") as dat:
        dat["list"] = rnd


if __name__ == "__main__":
    main()
