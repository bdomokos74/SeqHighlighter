import StringIO
import sys
from Bio import SeqIO
import json
from cStringIO import StringIO

def read_fasta(fname):
    result = []
    with open(fname, "rU") as f:
        fasta = SeqIO.parse(f, "fasta")
        for contig in fasta:
            sys.stderr.write("Reading %s\n"%(contig.name))
            result.append((contig.name, str(contig.seq).upper()))
    return(result)

def main():
    fasta_name = sys.argv[1]
    res = read_fasta(fasta_name)
    with open("run/multiseq.js", 'w') as out:
        out.write("<script type='javascript'>\n")
        out.write("var multiseq = ")
        json.dump(res, out)
        out.write(";\n</script>\n")


if __name__ == "__main__":
    main()