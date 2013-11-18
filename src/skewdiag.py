import sys

class GenomeSkew:
    def __init__(self, fname):
        self.genome = fname
        self.curr_skew = 0
        self.skew = [0]
        self.curr_pos = 0
        self.generate_skew_diag()

    def calc_skew(self, seq):
        for ch in seq:
            if ch=="C":
                self.curr_skew -= 1
            elif ch=="G":
                self.curr_skew += 1
            self.skew.append(self.curr_skew)

    def generate_skew_diag(self):
        f = open(self.genome, 'r')
        for line in f:
            if line[0] == ">":
                continue
            self.calc_skew(line.strip())
        f.close()

    def get_result(self, n):
        result = []
        i = 0
        l = len(self.skew)
        step = l/n
        while i+step < l:
            avg = 0
            for j in range(step):
                avg += self.skew[i+j]
            result.append((i, i+step, 1.0*avg/step))
            i += step
        sys.stderr.write( "last = %d\n"%(i))
        return (result)

def main():
    g = GenomeSkew(sys.argv[1])
    circos = False
    if len(sys.argv)>3:
        if sys.argv[2] == "-c":
            circos = True
            contig = sys.argv[3]

    if not circos:
        print "pos,skew"
    for v in g.get_result(1000):
        if circos:
            print "%s %d %d %d"%(contig, v[0], v[1], v[2])
        else:
            print "%d,%d"%((v[0]+ v[1])/2, v[2])

if __name__ == "__main__":
    main()
