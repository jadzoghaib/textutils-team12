# textutils-team12

Small Python package for text utilities — group assignment

## Team Members
•⁠  ⁠Jad Zoghaib (@jadzoghaib) - Repository Owner
•⁠  ⁠Miguel de Faria (@marinmiguel)
•⁠  ⁠Ana Petrescu (@anaapetrescu)
•⁠  ⁠Jan Philipp Gnau (@Thisisntevenmyfinale)



## Features 

Our package includes the following text utility functions:

•⁠  ⁠⁠ slugify(text) — convert text to lowercase, hyphen-separated safe string
•⁠  ⁠⁠ entence_count(text) — count number of sentences in text
•⁠  ⁠⁠ word_count(text) — case-insensitive counts
•⁠  ⁠⁠ is_palindrome(text) — check if text reads the same backwards (ignore case and spaces)
•⁠  ⁠⁠ count_vowels(text) — count vowels in the given text

## Installation

### 1. Create the repository
Create new public repository on Github (textutils-team12)
   * Add a `.gitignore` for Python and a short description like:

### 2. Clone the repository
git clone https://github.com/ayush/textutils-2.git
cd textutils-team12
 ⁠

### 3. Create the environment
⁠micromamba create -f textutils.yml -y
micromamba activate textutils
 ⁠

### 4. Install the package
pip install -e
 ⁠

## 5. Running Tests
Running all tests:
pytest

To see detailed coverage information:
pytest --cov=src/textutils --cov-report=term-missing
  ⁠

## Included Functionalities
import re
import unicodedata
from collections import Counter

### Slugify
def slugify(text):
    text = unicodedata.normalize('NFD', text)
    text = ''.join(c for c in text if unicodedata.category(c) != 'Mn')
    text = text.lower()
    text = re.sub(r'&', 'and', text)
    text = re.sub(r'[^a-z0-9]+', '-', text)
    return text.strip('-')

### Sentence Count
def sentence_count(text):
    sentences = re.split(r'[.!?]+', text.strip())
    return len([s for s in sentences if s.strip()])

### Word Count
def word_count(text):
    words = text.lower().split()
    return dict(Counter(words))

### Palindrome Checker
def is_palindrome(text):
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

### Vowels Count
def count_vowels(text):
    vowels = "aeiou"
    return sum(1 for char in text.lower() if char in vowels)
⁠

### Development

This assignment was developed as a collaboratively using:
•⁠  ⁠Test-Driven Development
•⁠  ⁠Seperate branch workflows for each functionality
•⁠  ⁠Git version control
•⁠  ⁠Continuous testing with pytest

### Project Description and Encountered Difficulties
Class project for ESADE.
