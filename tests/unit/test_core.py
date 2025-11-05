def slugify(text):
    import re
    import unicodedata
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    text = text.lower()
    text = re.sub(r'&', 'and', text)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')
