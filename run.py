#!/usr/bin/env python3

import argparse

from modules import config
from modules.cerfaReader import CerfaReader
from modules.cerfaWriter import CerfaWriter


def parse_arg():

    parser = argparse.ArgumentParser(description='Personal information')
    parser.add_argument('-i', '--input', dest='input_file', type=str, help='path to the input Cerfa file to read.')
    parser.add_argument('-o', '--output', dest='output_file', type=str, help='path to the output Cerfa file to write.')

    return parser.parse_args()


def main() -> None:

    args = parse_arg()
    if (not args.input_file) or (not args.output_file):
        print("Error: you need to give the input and ouput file for processing.")
        return

    reader = CerfaReader(args.input_file)
    writer = CerfaWriter(args.output_file, config.label_match_dict)

    writer.annotate(reader.get_annot_dict())

if __name__ == '__main__':
    main()
