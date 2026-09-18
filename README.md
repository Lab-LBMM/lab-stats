# lab-stats
this script needs a enviroment to run, to create and activate the enviromente, run:

```
python3 -m venv .venv
source .venv/bin/activate
```

Running the script:

to run the script you will need an input in a format that pandas can read (ex: .txt, .csv, .xls or google sheets link, the sheet needs to be public to work).

the terminal command will look like this:

```
python3 XXXX_stats.py -i link/file -g graph
```

"python3" = specifies the language to be used.
"XXXX_stats.py" = specifies the script that will de used
"-i link/file" = the input file or link.
"-g graph" = sinagnals if a graph is required, his name, his destiny and his format(optional).

if you run the entire command with input and graph, you will a files containing the graph.