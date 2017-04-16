# write select number of top BLAST results from xml search results to a txt file 
import sys
from Bio.Blast import NCBIXML
infile = str(sys.argv[1]) # select .xml file w/ blast results
outfile = str(sys.argv[2]) # specify output file
blast_result = open(infile)
records = NCBIXML.parse(blast_result)
item = next(records)
output_file = outfile

count = 0 # number of results from initial BLAST search - in input file

i = 0 # numbering records that are written
with open(output_file, "w") as f:
	for alignment in item.alignments:
		count += 1
	print "You have %d records in the original BLAST file: " % count
	list_num = int(raw_input("How many records would you like to see? >"))
	for alignment in item.alignments[:list_num]: #slicing in the top 4 aligments
		for hsp in alignment.hsps:
			if hsp.expect <0.01:
					f.write("You have %d total records in the original BLAST output file. \n" %count)
					f.write("This file contains the first %d records. \n" % list_num)
					f.write("**Alignment with Seq3 " + str(i+1) + "**" + "\n") # print each alignment w/ number
					f.write("sequence:" + str(alignment.title) + "\n")
					f.write("length:" + str(alignment.length) + "\n")
					f.write("score:" + str(hsp.score) + "\n")
					f.write("gaps:" + str(hsp.gaps) + "\n")
					f.write("e value:" + str(hsp.expect) + "\n\n")
	# printing out aligment 100 bases/line
					f.write(hsp.query[0:100] + "\n")
					f.write(hsp.match[0:100] + "\n")
					f.write(hsp.sbjct[0:100] + "\n\n")
					f.write(hsp.query[101:200] + "\n")
					f.write(hsp.match[101:200] + "\n")
					f.write(hsp.sbjct[101:200] + "\n\n")
					f.write(hsp.query[201:300] + "\n")
					f.write(hsp.match[201:300] + "\n")
					f.write(hsp.sbjct[201:300] + "\n\n")
					f.write(hsp.query[301:400] + "\n")
					f.write(hsp.match[301:400] + "\n")
					f.write(hsp.sbjct[301:400] + "\n\n")
					f.write(hsp.query[401:500] + "\n")
					f.write(hsp.match[401:500] + "\n")
					f.write(hsp.sbjct[401:500] + "\n\n")
					f.write(hsp.query[501:600] + "\n")
					f.write(hsp.match[501:600] + "\n")
					f.write(hsp.sbjct[501:600] + "\n\n")
					f.write(hsp.query[601:700] + "\n")
					f.write(hsp.match[601:700] + "\n")
					f.write(hsp.sbjct[601:700] + "\n\n")
					f.write(hsp.query[701:800] + "\n")
					f.write(hsp.match[701:800] + "\n")
					f.write(hsp.sbjct[701:800] + "\n\n")
					f.write(hsp.query[801:900] + "\n")
					f.write(hsp.match[801:900] + "\n")
					f.write(hsp.sbjct[801:900] + "\n\n")
					f.write(hsp.query[901:1000] + "\n")
					f.write(hsp.match[901:1000] + "\n")
					f.write(hsp.sbjct[901:1000] + "\n\n")
			i += 1
