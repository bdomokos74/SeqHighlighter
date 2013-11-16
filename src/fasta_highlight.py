import StringIO
import sys
from Bio import SeqIO
import json
from cStringIO import StringIO

def gen_html_seq(seq, freq, line_width=60):
    str = StringIO()
    line_pos = 0
    str_pos = 0
    for ch in list(seq):
        str.write("<span class=\"nucleotide\" id=\"nuc_%d\">%s</span>"%(str_pos, ch))
        line_pos += 1
        str_pos += 1

        if line_pos==line_width:
            str.write("<br/>\n")
            line_pos=0
    return(str.getvalue())

def main():
    fasta_name = sys.argv[1]
    freq_name = sys.argv[2]
    title = sys.argv[3]
    kvalue = sys.argv[4]
    template_name = "src/hltemplate.html"

    with open(fasta_name, "rU") as f:
        fasta = SeqIO.parse(f, "fasta")
        contig = fasta.next()
        sys.stderr.write("Reading %s\n"%(contig.name))
        seq = str(contig.seq).upper()



    with open(freq_name, "r") as f:
        freq_str = f.read()

    with open(freq_name, "r") as f:
        freq = json.load(f)

    html_seq = gen_html_seq(seq, freq)

    with open(template_name, "r") as f:
        template = f.read()
        processed = template.replace("@@seq@@", html_seq)
        processed = processed.replace("@@title@@", title)
        processed = processed.replace("@@kvalue@@", kvalue)
        processed = processed.replace("@@seqlen@@", str(len(seq)))
        processed = processed.replace("@@kmers@@", freq_str)
        print processed

if __name__ == "__main__":
    main()