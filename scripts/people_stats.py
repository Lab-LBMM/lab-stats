#!/usr/bin/env python3

import re
import argparse
import pandas as pd
import matplotlib.pyplot as plt

def converter_link_da_planilha(linkoucaminho):

    guia = "1260269705"

    if "docs.google.com/spreadsheets" in linkoucaminho:
        match = re.search(r"/d/([a-zA-Z0-9-_]+)", linkoucaminho)
        if match:
            sheet_id = match.group(1)
            return f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={guia}"
    return linkoucaminho

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

fonte_dados = converter_link_da_planilha(args.input)
if fonte_dados.startswith("http"):
    dados_df = pd.read_csv(fonte_dados)
else:
    dados_df = pd.read_table(fonte_dados)

print(dados_df.head)

if args.grafico:
    titulo = input("Digite o título do gráfico: ")
    
    dados_df['categoria'].value_counts().plot(
        kind="pie", 
        autopct="%1.1f%%", 
        title=titulo,
        fontsize=14
    )
    plt.ylabel("")
    plt.savefig(args.grafico, bbox_inches="tight")
    plt.close()
    print(f"Gráfico salvo em: {args.grafico}")

"python3 lab-stats/scripts/people_stats.py -i https://docs.google.com/spreadsheets/d/1cW5kMDnVopYCvaTLuohK-kUd_aveG5gR5KwLWJEx3iI/edit?gid=0#gid=0 -g lab-stats/files/graficotestealfapeople"