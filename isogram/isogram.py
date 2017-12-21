def is_isogram(string):
	lwString = string.lower()

	for i in range(len(lwString)):
		for j in range(i+1,len(lwString)):
			if lwString[i] != " " and lwString[i] != "-" and lwString[i] == lwString[j]:
				# print("char at " + str(i) + ": " + lwString[i] + " returned False for word: " + lwString)
				return False
	return True
