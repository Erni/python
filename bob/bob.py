def hey(phrase):
	stripped_phrase = phrase.strip()

	if stripped_phrase == '':
		return 'Fine. Be that way!'

	alpha_phrase = ''
	for c in stripped_phrase:
		if c.isalpha():
			alpha_phrase += c
	if alpha_phrase.isupper():
		return 'Whoa, chill out!'

	if stripped_phrase.endswith('?'):
		return 'Sure.'

	return 'Whatever.'
