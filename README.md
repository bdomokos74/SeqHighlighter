SeqHighlighter
==============

Tool for visualising frequent genomic sequences.

Required
========
- Python
- BioPython module (easy_install biopython)

Running
=======
From the project root run the following:

python src/fasta_highlight.py data/ecoli_oric.fa data/ecoli_oric_kmers_k9_d1.json \
    "E. coli oriC" 9 > results/ecoli_oric_k9_d1.html

python src/fasta_highlight.py data/ssop2_oric1.fa data/ssop2_oric1_kmers_k9_d1.json \
    "S. solfataricus oriC 1" 9 > ssop2_oric1_k9_d1.html

Examples
========


