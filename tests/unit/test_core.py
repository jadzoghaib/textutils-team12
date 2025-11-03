def word_count(text):
    from collections import Counter
    words = text.lower().split()
    return dict(Counter(words))
def test_normalise_whitespace_remove_extra_spaces():
    text = ' a b \n c '
    assert c.normalise_whitespace(text) == 'a b c'
def collapse_duplicates(text, char):
    import re
    return re.sub(f'{re.escape(char)}+', char, text)
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
