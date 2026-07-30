#!/usr/bin/env python3

import argparse
import pandas as pd

parser = argparse.ArgumentParser(
    description=__doc__
)
parser.add_argument(
    "-i", "--input",
    type=str,
    required=True,
    help="Path to the input file",
)
parser.add_argument(
    "-o", "--output",
    type=str,
    required=True,
    help="Path to the output file or directory",
)
parser.add_argument(
    "--version",
    action="version",
    version="%(prog)s 0.1.0",
)

args = parser.parse_args()

