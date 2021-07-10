from PIL import Image
import numpy as np
import pandas as pd
import os

from helper import *

import argparse

import matplotlib.pyplot as plt


def main():

    parser = argparse.ArgumentParser(
        description="""
        This program takes an input image, and a folder path and generate a mosiac image
        using the images in the folder as color tiles.
    
    """,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    parser.add_argument('input', type=str, help="the input image file")

    parser.add_argument('folder',
                        type=str,
                        help="the path to the database folder.")

    parser.add_argument(
        '-o',
        '--output',
        type=str,
        default='output.jpg',
        help="the path to the output file, the default is output.jpg")

    parser.add_argument('-t',
                        '--tile_size',
                        type=int,
                        default=10,
                        help="size of mosiac tiles, the default is 10")

    parser.add_argument(
        '-s',
        '--size',
        type=int,
        default=500,
        help=
        "the width of the image, the default is 500, and the height is calculated by ratio"
    )

    parser.add_argument('-sh',
                        '--show',
                        action="store_true",
                        help="show image upon completion")

    args = parser.parse_args()

    tile_s = (args.tile_size, args.tile_size)

    if not os.path.exists("database.csv"):
        df = create_data_base(args.folder)
        df.to_csv("database.csv")

    else:
        df = pd.read_csv("database.csv")

    image = Image.open(args.input)

    image = image.resize(
        (args.size, int(args.size / image.size[0] * image.size[1])))

    np_img = np.array(image)

    t_img = tilize_image(np_img, tile_s)

    output = mosaic(t_img, tile_s, df)

    plt.figure()
    plt.imshow(output / 255)
    plt.savefig("output.jpg")

    if args.show:
        plt.show()


if __name__ == "__main__":
    main()
