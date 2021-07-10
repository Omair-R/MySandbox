import argparse
from utils import *

def main() -> None:

    parser = argparse.ArgumentParser(
        description="""
        Not much honestly, just a program that takes an image and turns
        it into a nice ACSII art text, I needed it for my chat rooms. It has some bugs
        that I will probably never fix, sorry XD
         """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="enjoy! X3",
    )

    parser.add_argument("input", type=str, help="The input file")

    parser.add_argument(
        "-w",
        "--width",
        default=20,
        type=int,
        help="width of the desired image, default is 20",
    )
    parser.add_argument(
        "-hi",
        "--height",
        default=0,
        type=int,
        help="height of the desired image, the default will be calculated from the width.",
    )
    parser.add_argument(
        "-s",
        "--scale",
        default=2,
        type=int,
        help="ration of width to height in terms of block, default is 2 (best).",
    )
    parser.add_argument(
        "-e",
        "--exact",
        action="store_true",
        help="the width isn't always exactly as inputted due to the limitations of charaters, if you still wish to keep it exact there will be a loss of about two cols",
    )
    parser.add_argument(
        "-l",
        "--level",
        default=70,
        choices=[10, 70],
        type=int,
        help="The level of grayscale characters, only 10 or 70 are available.",
    )
    parser.add_argument(
        "-o",
        "--output",
        default="output.txt",
        type=str,
        help="output file, preferably a txt file.",
    )
    parser.add_argument(
        "-p",
        "--print",
        action="store_true",
        help="prints the encoded image into the console.",
    )

    args = parser.parse_args()

    img = encoder(args.input, args.width, args.height, args.scale, args.exact,
                  args.level)

    if args.print:
        print(img)

    save_to_file(img, args.output)


if __name__ == "__main__":
    main()
