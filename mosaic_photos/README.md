# Project

This project simple generates mosaic art from a foldar of images that are inputed into it. 

## Usage

```terminal
>>> python mosaic.py -h
usage: mosaic.py [-h] [-o OUTPUT] [-t TILE_SIZE] [-s SIZE] [-sh] input folder

        This program takes an input image, and a folder path and generate a mosiac image
        using the images in the folder as color tiles.



positional arguments:
  input                 the input image file
  folder                the path to the database folder.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        the path to the output file, the default is output.jpg
  -t TILE_SIZE, --tile_size TILE_SIZE
                        size of mosiac tiles, the default is 10
  -s SIZE, --size SIZE  the width of the image, the default is 500, and the height is calculated by ratio
  -sh, --show           show image upon completion

```
