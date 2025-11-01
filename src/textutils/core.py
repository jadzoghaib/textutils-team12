def unique_words(text):
    words = text.lower().split()
    words = [word.strip(".,!?;:'\"()[]{}") for word in words]
    return sorted(set(words))
