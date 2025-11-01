def strip_accents(text):
    import unicodedata
    normalized = unicodedata.normalize('NFD', text)
    
    return ''.join(
        char for char in normalized
        if unicodedata.category(char) != 'Mn'
    )
