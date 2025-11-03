def collapse_duplicates(text, char):
    import re
    return re.sub(f'{re.escape(char)}+', char, text)
