def replace_numbers(text):
    words = {'0':'zero','1':'one','2':'two','3':'three','4':'four',
             '5':'five','6':'six','7':'seven','8':'eight','9':'nine'}
    result = []
    for char in text:
        if char in words:
            if result and result[-1] != ' ':
                result.append(' ')
            result.append(words[char])
            if char != text[-1] and text[text.index(char) + 1] != ' ':
                result.append(' ')
        else:
            result.append(char)
    return ''.join(result).replace('  ', ' ').strip()