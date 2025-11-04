import textutils.core as c

def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
def word_count(text):
    from collections import Counter
    words = text.lower().split()
    return dict(Counter(words))
def sentence_count(text):
    import re
    sentences = re.split(r'[.!?]+', text.strip())
    return len([s for s in sentences if s.strip()])

def test_normalise_whitespace_remove_extra_spaces():
    text = ' a b \n c '
    assert c.normalise_whitespace(text) == 'a b c'
def collapse_duplicates(text, char):
    import re
    return re.sub(f'{re.escape(char)}+', char, text)

def test_count_vowels_basic():
    assert c.count_vowels("hello") == 2
    assert c.count_vowels("sky") == 0
    assert c.count_vowels("AEIOU") == 5

def test_count_vowels_mixed_text():
    assert c.count_vowels("Python 3.12!") == 1
    assert c.count_vowels("bcd fgh") == 0
    assert c.count_vowels("aEiOu") == 5
