def word_count(text):
    from collections import Counter
    words = text.lower().split()
    return dict(Counter(words))
