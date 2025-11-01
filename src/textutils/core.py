def capitalize_sentences(text):
    import re
    sentences = re.split('([.!?] *)', text)
    capitalized_sentences = [s.capitalize() for s in sentences]
    return ''.join(capitalized_sentences)
