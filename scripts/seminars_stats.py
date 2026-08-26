#!/usr/bin/env python3

import matplotlib.pyplot as plt
import pandas as pd
import argparse

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
    required=True,
    help="image used to name graph(like: results.png)",
)

args = parser.parse_args()

#indicando o arquivo a ser lido
dados_df = pd.read_table(args.input)

#definindo o tamanho do gráfico
plt.figure(figsize=(10, 8))

#ajustando as características gerais
plt.bar(dados_df['Categoria'], dados_df['total'], color='blue', width= 0.5)

#configurando as legendas
plt.rc('xtick', labelsize=12)
plt.rc('ytick', labelsize=12) 
plt.xlabel('Categoria', fontsize=14, labelpad=14)
plt.ylabel('Quantidade de artigo', fontsize=14, labelpad=14)
plt.title('Seminário Online', fontsize=16)

plt.savefig(args.grafico)


