def decode(string):
	decoded = ''
	count = ''

	for c in string:
		if c.isalpha() or c == ' ':
			if(count == ''):
				count = '1'
			decoded += c * int(count)
			count = ''
		else:
			count += c
	return decoded


def encode(string):
	encoded = ''
	prev = ''
	count = 0
	current = ''

	for c in string:
		current = c
		if c != prev:
			if count > 1:
				encoded += str(count)
			encoded += prev
			prev = c
			count = 1
		else:
			count += 1

	if count > 1:
		encoded += str(count)
	encoded += current

	return encoded