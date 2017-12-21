import string

def is_pangram(sentence):
	lwSentence = sentence.lower()

	for c in string.ascii_lowercase:
		if c.isalpha() and c not in lwSentence:
			# print("False due to char: " + c + ". In sentence: " + lwSentence)
			return False
	return True
