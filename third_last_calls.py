import json
from pathlib import Path
from datetime import datetime


# 3.2
def main():
    calls_path = Path("calls.json")

    try:
        with calls_path.open("r") as calls_file:
            previous = json.load(calls_file)
    except FileNotFoundError:
        previous = {'times': []}
        print("It's first time you running this program!")

    for i in range(min(len(previous['times']), 3)):
        print(previous['times'][i])

    previous['times'].insert(0, str(datetime.now()))

    with calls_path.open("w") as calls_file:
        json.dump(previous, calls_file, indent=4)


if __name__ == "__main__":
    main()
