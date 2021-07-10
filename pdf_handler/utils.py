import PyPDF2
import win32com.client
import os

"""
- compression of pdfs
"""


def pdf_namer(pdf_name: str, adder: str) -> str:
    return os.path.abspath(pdf_name[:-4] + "_" + adder + ".pdf")


def merge_pdfs(pdf_file_in: str, pdf_file_out: str = "default") -> None:
    """ merges multiple pdfs into one pdf file."""

    pdf_list = pdf_file_in
    merger = PyPDF2.PdfFileMerger()

    for pdf in pdf_list:
        merger.append(pdf)

    if pdf_file_out == "default":
        pdf_file_out = os.path.join(
            os.path.dirname(pdf_file_in[0]), "merged.pdf")

    out = merger.write(pdf_file_out)

    print("\n process was a success!!")


def one_page_out(
    pdf_file_in: str, pdf_file_out: str = "default", page_index: int = 0
) -> None:
    """ Gets one page out of a pdf file into its own file."""

    pdf = PyPDF2.PdfFileReader(pdf_file_in)
    page = pdf.getPage(page_index)

    if pdf_file_out == "default":
        pdf_file_out = pdf_namer(pdf_file_in, str(page_index))

    pdf_writer = PyPDF2.PdfFileWriter()
    pdf_writer.addPage(page)

    with open(pdf_file_out, "wb") as file:
        pdf_writer.write(file)

    print("\n process was a success!!")


def split_at(pdf_file_in: str, page_index: int = 1) -> None:
    """ splits one pdf file into mutliple pdf files. """

    pdf = PyPDF2.PdfFileReader(pdf_file_in)
    page_numbers = pdf.getNumPages()
    pdfs_out = (PyPDF2.PdfFileWriter(), PyPDF2.PdfFileWriter())

    for n in range(0, page_index):
        page = pdf.getPage(n)
        pdfs_out[0].addPage(page)

    for n in range(page_index, page_numbers):
        page = pdf.getPage(n)
        pdfs_out[1].addPage(page)

    with open(pdf_namer(pdf_file_in, str(1)), "wb") as file:
        pdfs_out[0].write(file)

    with open(pdf_namer(pdf_file_in, str(2)), "wb") as file:
        pdfs_out[1].write(file)

    print("\n process was a success!!")


def encrypt_pdf(pdf_file_in: str, password: str, pdf_file_out: str = "default") -> None:
    """ encrypts a pdf file with a password """

    pdf = PyPDF2.PdfFileReader(pdf_file_in)

    page_numbers = pdf.getNumPages()

    pdf_writer = PyPDF2.PdfFileWriter()

    for n in range(page_numbers):
        page = pdf.getPage(n)
        pdf_writer.addPage(page)

    pdf_writer.encrypt(password)

    if pdf_file_out == "default":
        pdf_file_out = pdf_namer(pdf_file_in, "encrypted")

    with open(pdf_file_out, "wb") as file:
        pdf_writer.write(file)

    print("\n process was a success!!")


def decrypt_pdf(pdf_file_in: str, password: str, pdf_file_out: str = "default") -> None:
    """ decrypts a pdf file with a password """

    pdf = PyPDF2.PdfFileReader(pdf_file_in)

    if pdf.isEncrypted:
        response = pdf.decrypt(password)

        if response == 0:
            raise Exception("Wrong password, please re-enter the password.")

        pdf_writer = PyPDF2.PdfFileWriter()

        page_numbers = pdf.getNumPages()

        for n in range(page_numbers):
            page = pdf.getPage(n)
            pdf_writer.addPage(page)

        if pdf_file_out == "default":
            pdf_file_out = pdf_namer(pdf_file_in, "decrypted")

        with open(pdf_file_out, "wb") as file:
            pdf_writer.write(file)

        print("\n process was a success!!")


def pdf_to_word(pdf_file_in: str, pdf_file_out: str = "default") -> None:
    """ converts a pdf into a word file using Microsoft Word. """

    word = win32com.client.Dispatch("Word.Application")
    word.visible = 0

    document = word.Documents.Open(pdf_file_in, ReadOnly=True)

    if pdf_file_out == "default":
        pdf_file_out = os.path.abspath(pdf_file_in[:-4] + ".docx")

    document.SaveAs2(pdf_file_out, FileFormat=16)  # file format for docx
    document.Close()
    word.Quit()

    print("\n process was a success!!")
