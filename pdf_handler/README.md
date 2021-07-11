
## Usage

```
usage: pdf_handler.py [-h] [-o OUTPUT] {merge,split,decrypt,encrypt,pdf2word,page_out} input [input ...]

    ------------------------
    This program is just a basic pdf handler for automating some of the tedious work
    that I have to perform on a daily basis. All of these features might be found in
    other software, but I couldn't find one that is free. if you wish to use this program
    then go ahead :3

    ------------------------
    What can the program do?

    merge       === merges multiple files into one, the input should be a list of pdfs.
    split       === splits a file into two files when you provide an index, the input should be a pdf file and the index
    page_out    === gets one page out of a file, into its own one-page file, the input should be a pdf file and the index.
    decrypt     === self-explanatory, the input ist the pdf file and the password.
    encrypt     === self-explanatory, the input ist the pdf file and the password.
    pdf2word    === self-explanatory, the input should be a pdf file only, any other inputs will be ignored.

    ----------
    please read the help notes for each argument before using the program.

    Note: this hasn't been tested thoroughly yet, so please back up your file.



positional arguments:
  {merge,split,decrypt,encrypt,pdf2word,page_out}
                        choose the action you wish to perform
  input                 the input pdf file, and arguments.

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        the name of the output file.
 ```
