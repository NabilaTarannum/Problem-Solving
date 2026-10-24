def is_vowel(letter):
    return letter in "aeiouy"


def score_words(words):
    score = 0
    for word in words:
        num_vowels = sum(bool(is_vowel(letter)) for letter in word)
        score += 2 if num_vowels % 2 == 0 else 1
    return score


n = int(input())
words = input().split()
print(score_words(words))
