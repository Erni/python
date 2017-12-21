def word_count(phrase):
	clean_phrase = ''

	for c in phrase:
		if c.isalnum():
			clean_phrase += c.lower()
		elif c == ' ' or c == '\'':
			clean_phrase += c
		else:
			clean_phrase += ' '

	splitted_phrase = clean_phrase.split()

	result = {}

	for word in splitted_phrase:
		strippedWord = word.strip("'")
		if strippedWord in result:
			result[strippedWord] += 1
		else:
			result[strippedWord] = 1

	return result
