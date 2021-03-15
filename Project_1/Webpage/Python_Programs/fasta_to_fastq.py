#! /usr/bin/env python
import argparse

def run(args):
	filename = args.input # these match the "dest": dest="input"
	output_filename = args.output # from dest="output"
	qual = args.quality_score # default is I

	# Do stuff


def main():
	parser=argparse.ArgumentParser(description="Convert a fastA file to a FastQ file")
	parser.add_argument("-in",help="fasta input file" ,dest="input", type=str, required=True)
	parser.add_argument("-out",help="fastq output filename" ,dest="output", type=str, required=True)
	parser.add_argument("-q",help="Quality score to fill in (since fasta doesn't have quality scores but fastq needs them. Default=I" ,dest="quality_score", type=str, default="I")
	parser.set_defaults(func=run)
	args=parser.parse_args()
	args.func(args)

if __name__=="__main__":
	main()







"""
def run(args):
    	qual = args.quality_score
	f = open(args.input)
	fout = open(args.output, "w")
	seq = ""
	for line in f:
		if line[0] == ">":
			if seq != "":
				fout.write(seq + "\n")
				fout.write("+\n")
				fout.write(qual * len(seq) + "\n")
			fout.write("@" + line[1:])
			seq = ""
		else:
			seq += line.strip()
	f.close()

	fout.write(seq + "\n")
	fout.write("+\n")
	fout.write(qual * len(seq) + "\n")
	fout.close()
"""