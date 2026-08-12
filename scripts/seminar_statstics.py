#!/usr/bin/env python3

import argparse
import pandas as pd
import matplotlib.pyplot as plt
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
    required=False,
    help="Path to the output file or directory",
)
parser.add_argument(
    "--version",
    action="version",
    version="%(prog)s 0.1.0",
)
parser.add_argument(
    "-g", "--grafico",
    type=str,
    required=False,
    help="image used to name graph(like: results.png)",
)
args = parser.parse_args()
