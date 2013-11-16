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

```bash
python src/fasta_highlight.py data/ecoli_oric.fa data/ecoli_oric_kmers_k9_d1.json \
    "E. coli oriC" 9 > results/ecoli_oric_k9_d1.html

python src/fasta_highlight.py data/ssop2_oric1.fa data/ssop2_oric1_kmers_k9_d1.json \
    "S. solfataricus oriC 1" 9 > results/ssop2_oric1_k9_d1.html
```


Examples
========

[E. coli oriC](https://dl.dropboxusercontent.com/u/21726609/SeqHighlighter/ecoli_oric_k9_d1.html)

[Aeropyrum pernix K1 oriC](https://dl.dropboxusercontent.com/u/21726609/SeqHighlighter/apernixk1_oric_k10_d1.html)

[Pyrococcus abyssi GE5 oriC](https://dl.dropboxusercontent.com/u/21726609/SeqHighlighter/pabyssige5_oric_k9_d1.html)

[S. solfataricus oriC 1](https://dl.dropboxusercontent.com/u/21726609/SeqHighlighter/ssop2_oric1_k9_d1.html)

[S. solfataricus oriC 2](https://dl.dropboxusercontent.com/u/21726609/SeqHighlighter/ssop2_oric2_k9_d1.html)

[S. solfataricus oriC 3](https://dl.dropboxusercontent.com/u/21726609/SeqHighlighter/ssop2_oric2_k9_d1.html)
