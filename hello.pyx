def say_hello(name):
	return "Hello %s!" % name

def word_analyser(data):
	words_list = data.split()
	word_frequency = {}
	for word in words_list:
		if word in word_frequency:
			word_frequency[word] += 1
		else:
			word_frequency[word] = 1
	return word_frequency