# lab-stats
O repositório Lab-Stats foi criado para a apresentação gráfica de atividades desenvolvidas pelo LBMM (como seminários e minicursos) e da produção científica. A criação de gráficos por si só é uma atividade prática para os iniciantes em programação.
Todos os scripts desenvolvidos estão presentes no Github.

Para fazer uso dos scripts é necessário o uso de um ambiente python3, que pode ser criado utilizando os seguintes comandos no terminal:

```
python3 -m venv .venv
source .venv/bin/activate
```

Rodando o script:

Para utilizar o script é preciso de um arquivo(.tsv, .csv, .txt) ou link de planilha do google sheets que será lido pela biblioteca pandas, um exemplo de arquivo é o lbmm_general.tsv na pasta files. Atualmente utilizamos a planilha pública https://docs.google.com/spreadsheets/d/1cW5kMDnVopYCvaTLuohK-kUd_aveG5gR5KwLWJEx3iI/edit? como fonte de dados remota.
Os argumentos necessários são -i input, -g graph, caso deseje consultar a versão do script use --version, o comando se parecerá com isso:

```
python3 XXXX_stats.py -i link/arquivo -g gráfico
```

"python3" = específica a linguagem do programa.
"XXXX_stats.py" = específica o script a ser usado.
"-i link/arquivo" = o arquivo ou link de entrada.
"-g gráfico" = o nome, localização e formato(.png, .pdf) do gráfico a ser gerado.

O repositório está em constante desenvolvimento, sugestões, críticas e contribuições são sempre bem-vindas.