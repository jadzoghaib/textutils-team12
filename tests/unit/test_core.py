def collapse_duplicates(text, char):
    import re
    return re.sub(f'{re.escape(char)}+', char, text)
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]
