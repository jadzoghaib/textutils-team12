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

def count_vowels(text: str) -> int:
    """Count the number of vowels in a given text."""
    vowels = "aeiouAEIOU"
    return sum(1 for char in text if char in vowels)
