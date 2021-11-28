#!/usr/bin/env python3

from modules import config
from modules.cerfaReader import CerfaReader
from modules.cerfaWriter import CerfaWriter


def main():
    reader = CerfaReader("data/pdf_filled/old_sample.pdf")
    writer = CerfaWriter("output_test/output.pdf", "data/pdf_models/new_model_1.pdf", config.label_match_dict)

    writer.annotate(reader.get_annot_dict())

if __name__ == '__main__':
    main()
