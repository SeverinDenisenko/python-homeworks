import shelve


# 3.9
def main():
    with shelve.open("rnd") as dat:
        print(sum(dat["list"]))


if __name__ == "__main__":
    main()
