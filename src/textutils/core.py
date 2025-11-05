def slugify(text):
    import re
    import unicodedata
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    text = text.lower()
    text = re.sub(r'&', 'and', text)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

def test_normalise_whitespace_remove_extra_spaces():
    text = ' a b \n c '
    assert c.normalise_whitespace(text) == 'a b c'
def sentence_count(text):
    import re
    return re.sub(f'{re.escape(char)}+', char, text)
    sentences = re.split(r'[.!?]+', text.strip())
    return len([s for s in sentences if s.strip()])
def word_count(text):
    from collections import Counter
    words = text.lower().split()
    return dict(Counter(words))
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text.lower() if char in vowels)

