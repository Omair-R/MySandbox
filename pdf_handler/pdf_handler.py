import argparse
import sys
import os

from utils import *


def main():

    parser = argparse.ArgumentParser(
        description="""

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


    """,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "action",
        # metavar="action",
        choices=["merge", "split", "decrypt", "encrypt", "pdf2word", "page_out"],
        help="choose the action you wish to perform",
    )

    parser.add_argument(
        "input",
        nargs="+",
        type=str,
        help="the input pdf file, and arguments.",
    )

    parser.add_argument(
        "-o", "--output", help="the name of the output file.", default="default"
    )

    args = parser.parse_args()

    if not os.path.isfile(args.input[0]):
        raise Exception("this is not a valid file.")
        sys.exit()

    if args.action == "merge":
        merge_pdfs(args.input, pdf_file_out=args.output)

    elif args.action == "split":
        split_at(args.input[0], page_index=int(args.input[1]))

    elif args.action == "decrypt":
        decrypt_pdf(args.input[0], password=args.input[1], pdf_file_out=args.output)

    elif args.action == "encrypt":
        encrypt_pdf(args.input[0], password=args.input[1], pdf_file_out=args.output)

    elif args.action == "page_out":
        one_page_out(
            args.input[0], page_index=int(args.input[1]), pdf_file_out=args.output
        )

    else:
        pdf_to_word(pdf_file_in=args.input[0])


if __name__ == "__main__":
    main()