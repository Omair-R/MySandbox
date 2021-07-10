import sys
from PIL import Image
import numpy as np
import pandas as pd
import os
from typing import Tuple


def update_progress_bar(complete,
                        n_iterations,
                        block_shape="|",
                        remaining_shape="-",
                        len_bar=30):

    progress = complete / n_iterations

    rounded_progress = int(round(len_bar * progress))

    draw_progress = block_shape * rounded_progress + remaining_shape * (
        len_bar - rounded_progress)

    text = f"\r|{draw_progress}| {complete}/{n_iterations} {progress*100:2.2f}% "

    sys.stdout.write(text)
    sys.stdout.flush()


def rgb_average(image: np.array) -> np.array:
    shape = image.shape
    return np.average(np.resize(image, (shape[0] * shape[1], shape[2])),
                      axis=0)


def create_data_base(image_dir: str) -> pd.DataFrame:

    dir = os.listdir(image_dir)
    df = pd.DataFrame(columns=["image", "r", "b", "g"])

    for i, file in enumerate(dir):
        path = os.path.join(image_dir, file)
        try:
            im = Image.open(path)
            np_im = np.array(im)
            ave = rgb_average(np_im)
            df.loc[i] = [path, ave[0], ave[1], ave[2]]
        except:
            print(f"invalid image: {path}")

    return df


def tilize_image(image: np.array, tile_s: Tuple[int, int]) -> np.array:
    W, H, _ = image.shape
    m, n = tile_s
    w, h = W // m, H // n

    output_grid = np.empty((w, h, 3))
    for i in range(w):
        for j in range(h):
            output_grid[i, j] = rgb_average(image[i * m:(i + 1) * m,
                                                  j * n:(j + 1) * n])

    return output_grid


def match_averages(image_ave: np.array, df: pd.DataFrame) -> str:

    ave = np.array((df.loc[:]['r'], df.loc[:]['g'], df.loc[:]['b']))
    ave = ave.T
    dis = np.linalg.norm((image_ave - ave), axis=1)

    return df.loc[np.argmin(dis)]["image"]


def mosaic(tile_image: np.array, tile_s: Tuple[int, int],
           df: pd.DataFrame) -> np.array:

    w, h = tile_image.shape[0], tile_image.shape[1]
    m, n = tile_s
    W, H = w * m, h * n

    output = np.empty((W, H, 3))

    for i in range(w):
        for j in range(h):
            image_path = match_averages(tile_image[i, j], df)
            image = Image.open(image_path)
            image = image.resize(tile_s)
            output[i * m:(i + 1) * m, j * n:(j + 1) * n] = image

        update_progress_bar(i, tile_image.shape[0])

    return output
