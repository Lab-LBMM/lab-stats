#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import argparse
import re

#regularizar o link para o formato CSV

def converter_link_da_planilha(linkoucaminho):

    guia = "0"

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
    "--version",
    action="version",
    version="%(prog)s 0.1.0",
)
parser.add_argument(
    "-i", "--input",
    type=str,
    required=True,
    help="link ou arquivo de entrada",
)
parser.add_argument(
    "-g", "--graph",
    type=str,
    required=True,
    help="nome e formato do grafico",
)

args = parser.parse_args()

#dados
fonte_dados = converter_link_da_planilha(args.input)
if fonte_dados.startswith("http"):
    dados_df = pd.read_csv(fonte_dados)
else:
    dados_df = pd.read_table(fonte_dados)

#data para datetime
dados_df['data'] = pd.to_datetime(dados_df['data'], dayfirst=True)

#trimestres
dados_df['Trimestre'] = dados_df['data'].dt.to_period('Q').astype(str)

#grupo de trimentres
df_trimestral = dados_df.groupby('Trimestre').size().reset_index(name='total')

plt.figure(figsize=(10, 6))
plt.bar(df_trimestral['Trimestre'], df_trimestral['total'], color='royalblue', width=0.5)
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12) 
plt.xlabel('Trimestre', fontsize=14, labelpad=12)
plt.ylabel('Quantidade de Artigos', fontsize=14, labelpad=12)
plt.title('Total de artigos apresentados por trimestre', fontsize=16, pad=15)

for i, valor in enumerate(df_trimestral['total']):
    plt.text(i, valor + 0.1, str(valor), ha='center', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig(args.grafico)
plt.close()
print(f"Gráfico salvo em: {args.grafico}")

"python3 lab-stats/scripts/seminars_stats.py -i https://docs.google.com/spreadsheets/d/ ( id da planilha ) /edit?usp=sharing -g lab-stats/files/graficotestealfaseminars"