""" BLAST sequencing results for any fasta file - as argv """ 

from Bio.Blast import NCBIWWW
from Bio import SeqIO
import sys
search_fasta = str(sys.argv[1])
out_xml = str(sys.argv[2])
record = SeqIO.read(search_fasta, format="fasta")
blast_result = NCBIWWW.qblast("blastn", "nt", record.seq)
save_file = open(out_xml, "w")
save_file.write(blast_result.read())
save_file.close()
blast_result.close()

""" print out top 3 BLAST results """

blast_result = open("my_blast.xml")
from Bio.Blast import NCBIXML
records = NCBIXML.parse(blast_result)
item = next(records)

for alignment in item.alignments[:3]: #slicing in the top 3 aligments
	for hsp in alignment.hsps:
		if hsp.expect <0.01:
				print "**Alignment**"
				print "sequence:", alignment.title
				print "length:", alignment.length
				print "score:", hsp.score
				print "e value:", hsp.expect
				print "gaps:", hsp.gaps
# printing out aligment 100 bases/line
				print hsp.query[0:100] + '...' 
				print hsp.match[0:100] + '...'
				print hsp.sbjct[0:100] + '...'
				print hsp.query[101:200] + '...' 
				print hsp.match[101:200] + '...'
				print hsp.sbjct[101:200] + '...'
				print hsp.query[201:300] + '...' 
				print hsp.match[201:300] + '...'
				print hsp.sbjct[201:300] + '...'
				print hsp.query[301:400] + '...' 
				print hsp.match[301:400] + '...'
				print hsp.sbjct[301:400] + '...'































