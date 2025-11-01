def remove_punctuation(text):
    import string
    return text.translate(str.maketrans('', '', string.punctuation))
