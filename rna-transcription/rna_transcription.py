def to_rna(dna_strand):
	rna_trans = {'G' : 'C', 'C' : 'G', 'T' : 'A', 'A' : 'U' }
	rna_strand = ''

	for c in dna_strand:
		try:
			rna_strand += rna_trans[c]
		except:
			raise ValueError("Character " + c + " does not match any DNA nucleotide")
	return rna_strand

