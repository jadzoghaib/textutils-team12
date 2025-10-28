def word_count(text):
	"""Return a dictionary with the count of each word in `text`.

	Words are lower-cased and split on whitespace.

	Example:
		>>> word_count('Hello hello world')
		{'hello': 2, 'world': 1}
	"""
	from collections import Counter

	words = text.lower().split()
	return dict(Counter(words))

