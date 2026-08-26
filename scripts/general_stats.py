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

df = pd.read_csv(args.input, sep=",")

df_clean = df.dropna()

if args.grafico:
    gname = input("insert graph title: ")
    print(f"generating graph:{args.grafico}")
    df_clean.plot(kind='bar', x='categories', y='amount', color='green', title=gname)
    plt.gca().get_legend().remove()
    plt.savefig(args.grafico, bbox_inches='tight')
    plt.close()

# 
df_clean.to_csv(args.output, sep='\t', index=False)
