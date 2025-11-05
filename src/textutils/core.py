def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def count_vowels(text):
    vowels = "aeiouAEIOU"
    return sum(1 for char in text.lower() if char in vowels)

