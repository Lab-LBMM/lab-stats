#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import argparse
import re

#regularizar o link para o formato CSV

def converter_link_da_planilha(linkoucaminho):
    if "docs.google.com/spreadsheets" in linkoucaminho:
        match = re.search(r"/d/([a-zA-Z0-9-_]+)", linkoucaminho)
        if match:
            sheet_id = match.group(1)
            return f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv"
    return linkoucaminho

parser = argparse.ArgumentParser(
    description="Gera gráfico de barras por trimestre a partir de datas."
)
parser.add_argument(
    "-i", "--input",
    type=str,
    required=True,
    help="link",
)
parser.add_argument(
    "-g", "--grafico",
    type=str,
    required=True,
    help="image used to name graph(like: results.png)",
)

args = parser.parse_args()

#dados
fonte_dados = converter_link_da_planilha(args.input)
if fonte_dados.startswith("http"):
    dados_df = pd.read_csv(fonte_dados)
else:
    dados_df = pd.read_table(fonte_dados)

#Data para datetime
dados_df['Data'] = pd.to_datetime(dados_df['Data'], dayfirst=True)

#trimestres
dados_df['Trimestre'] = dados_df['Data'].dt.to_period('Q').astype(str)

#grupo de trimentres
df_trimestral = dados_df.groupby('Trimestre').size().reset_index(name='total')

plt.figure(figsize=(10, 6))
plt.bar(df_trimestral['Trimestre'], df_trimestral['total'], color='royalblue', width=0.5)
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12) 
plt.xlabel('Trimestre', fontsize=14, labelpad=12)
plt.ylabel('Quantidade de Artigos', fontsize=14, labelpad=12)
plt.title('Total de rtigos apresentados por rimestre', fontsize=16, pad=15)

for i, valor in enumerate(df_trimestral['total']):
    plt.text(i, valor + 0.1, str(valor), ha='center', fontsize=11, fontweight='bold')

plt.tight_layout()
plt.savefig(args.grafico)
print("sucesso")

"python3 lab-stats/scripts/testeseminar.py -i https://docs.google.com/spreadsheets/d/ ( id da planilha ) /edit?usp=sharing -g lab-stats/files/garficoteste"