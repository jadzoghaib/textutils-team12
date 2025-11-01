def word_lengths(text):
    words = text.split()
    return {word: len(word) for word in words}
