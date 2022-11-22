import argparse
from pathlib import Path


# 3.7
def main():
    parser = argparse.ArgumentParser(description='Find sizes if files in directory.')
    parser.add_argument('directory', type=str, help='Path to directory')
    args = parser.parse_args()

    directory = Path(args.directory)
    files = [f for f in directory.iterdir() if f.is_file()]
    sizes = [f.stat().st_size for f in files]
    # directory = args.directory
    # files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    # sizes = [os.path.getsize(f) for f in files]

    out = sorted(zip(sizes, files), reverse=True)

    for item in out:
        print(f"{str(item[1]):50} \t {item[0]}")


if __name__ == "__main__":
    main()
