def is_palindrome(word):
    clean_word = str(word).lower().replace(" ", "")
    return clean_word == clean_word[::-1]

