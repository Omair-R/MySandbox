# Project

This project simple generates ACSII art from images that are inputed into it. it runs on two levels of shading 70 and 10. 

## Usage

```terminal
>>> python Ascii_art.py -h
usage: Ascii_art.py [-h] [-w WIDTH] [-hi HEIGHT] [-s SCALE] [-e] [-l {10,70}] [-o OUTPUT] [-p] input

        Not much honestly, just a program that takes an image and turns
        it into a nice ACSII art text, I needed it for my chat rooms. It has some bugs
        that I will probably never fix, sorry XD


positional arguments:
  input                 The input file

optional arguments:
  -h, --help            show this help message and exit
  -w WIDTH, --width WIDTH
                        width of the desired image, default is 20
  -hi HEIGHT, --height HEIGHT
                        height of the desired image, the default will be calculated from the width.
  -s SCALE, --scale SCALE
                        ration of width to height in terms of block, default is 2 (best).
  -e, --exact           the width is not always exactly as inputted due to the limitations of charaters, if you still
                        wish to keep it exact there will be a loss of about two cols
  -l {10,70}, --level {10,70}
                        The level of grayscale characters, only 10 or 70 are available.
  -o OUTPUT, --output OUTPUT
                        output file, preferably a txt file.
  -p, --print           prints the encoded image into the console.

enjoy! X3

```
