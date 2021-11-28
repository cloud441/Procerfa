#!/usr/bin/env python3

from modules.cerfaReader import CerfaReader
from modules.cerfaWriter import CerfaWriter


def main():
    reader = CerfaReader("data/pdf_filled/old_sample.pdf")
    writer = CerfaWriter("output_test.pdf", {})


if __name__ == '__main__':
    main()
