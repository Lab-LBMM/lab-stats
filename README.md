# lab-stats
this script needs a enviroment to run, to create and activate the enviromente, run:

```
python3 -m venv .venv
source .venv/bin/activate
```

Running the script:

to run the script you will need an input in a format that pandas can read (ex: .txt, .csv, .xls, .json).

the terminal command will look like this:

```
python general_statistics.py -i lab_data.txt -o results.txt -g graph.png
```

"python" = specifies the language to be used.
"general_statistics.py" = specifies the script that will de used
"-i lab_data.txt" = the input.
"-o results.txt" = name of the resulting file(optional).
"-g graph.png" = sinagnals if a graph is required, his name and his format(optional).

if you run the entire command with input, output and graph, you will generate two files, one containing the graph and other containing a "cleaned" version of the input.