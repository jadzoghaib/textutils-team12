from textutils import core as c

def test_slugify_basic():
    assert c.slugify("Hello World") == "hello-world"

def test_slugify_special_chars():
    assert c.slugify("Hello & Goodbye!") == "hello-and-goodbye"

def test_sentence_count():
    assert c.sentence_count("Hello. How are you? I'm fine!") == 3

def test_word_count():
    result = c.word_count("hello world hello")
    assert result == {"hello": 2, "world": 1}

def test_is_palindrome():
    assert c.is_palindrome("racecar") == True
    assert c.is_palindrome("hello") == False

def test_count_vowels():
    assert c.count_vowels("hello") == 2
    assert c.count_vowels("AEIOU") == 5