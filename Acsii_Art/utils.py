from PIL import Image
import numpy as np
from typing import final
import os

LVL_10_GS: final = "@%#*+=-:. "
LVL_70_GS: final = """$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'. """


def average_pooling(img: np.array, factor: tuple) -> np.array:
    """
    Averages a pool in a matrix based on a specific factor of size N * L

    Args:
        img (np.array): The image to be pooled
        factor (tuple): the pooling factor

    Returns:
        pooled_img(np.array): the pooled image

    """
    W, H = img.shape
    w, h = W // factor[0], H // factor[1]

    img = img[:w * factor[0], :h * factor[1]]

    return img.reshape(w, factor[0], h,
                       factor[1]).mean(axis=(1, 3)).astype(int)


def encoder(img_path: str, width: int, height: int, scale: int, exact: bool,
            level: int) -> str:
    """
    The main encoder, it takes the image and its property and returns a string with the ASCII art. 

    Args:
        img_path (str): the path to the image.
        width (int): the width of the desired output.
        height (int): the height of the desired output.
        scale (int): factoring scale between the width and the height, multiplied by the width.
        exact (bool): the exact inputted columns.
        level (int): level of ACSII variety. 

    Returns:
        acsii_image(str): the final encoded image.
    """
    if not os.path.isfile(img_path):
        raise Exception("Input is not a file.")

    image = Image.open(img_path).convert("L")

    original_W, original_H = image.size

    if height == 0:
        height = int(original_H // (original_W // width))

    width *= scale
    factor = (original_H // height, original_W // width)

    avg_img = average_pooling(np.array(image), factor)

    ascii_image: str = str()

    if not exact:
        width = avg_img.shape[1]

    for i in range(height):
        if level == 70:
            for j in range(width):
                ascii_image += LVL_70_GS[avg_img[i, j] * 69 // 255]
        elif level == 10:
            for j in range(width):
                ascii_image += LVL_10_GS[avg_img[i, j] * 9 // 255]
        ascii_image += "\n"

    return ascii_image


def save_to_file(img_encoded: str, file_path: str) -> None:
    
    with open(file_path, "w") as file:
        file.write(img_encoded)
