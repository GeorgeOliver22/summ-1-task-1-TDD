import re

def is_palindrome(text):
    cleaned = re.sub(r'[^a-zA-Z-0-9]', '', text).lower()
    return cleaned == cleaned[::-1]
