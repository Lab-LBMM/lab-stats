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
    titulo = input("Digite o título do gráfico: ")
    
    df_clean["categoria"].value_counts().plot(
        kind="pie", 
        autopct="%1.1f%%", 
        title=titulo
    )
    plt.ylabel("")
    plt.savefig(args.grafico, bbox_inches="tight")
    plt.close()
    print(f"Gráfico salvo em: {args.grafico}")

if args.output:
    df_clean.to_csv(args.output, sep="\t", index=False)
    print(f"Arquivo salvo em: {args.output}")