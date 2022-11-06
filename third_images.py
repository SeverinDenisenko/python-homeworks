from urllib.request import urlopen
import argparse


# 3.8
def main():
    parser = argparse.ArgumentParser(description='Get jpeg from SDSS and save it to file on disk.')
    parser.add_argument('RA', type=float, help='right ascension')
    parser.add_argument('DEC', type=float, help='declination')
    parser.add_argument('--width', type=int, help='image width', default=512, required=False)
    parser.add_argument('--height', type=int, help='image height', default=512, required=False)
    parser.add_argument('--out', type=str, help='output file', default="out.jpeg", required=False)
    args = parser.parse_args()
    #  python3 third_images.py 13.5 10.2 --width 2048 --height 2048 --out hello.jpeg

    url = "http://skyserver.sdss.org/dr14/SkyServerWS/ImgCutout/getjpeg?"
    response = urlopen(f"{url}ra={args.RA}&dec={args.DEC}&width={args.width}&height={args.height}")

    with open(args.out, "wb") as out:
        out.write(response.read())


if __name__ == "__main__":
    main()
