def count_vowels(word):
    vowels = ['а', 'я', 'у', 'ю', 'о', 'е', 'ё', 'э', 'и', 'ы']
    count = 0
    for char in word:
        if char.lower() in vowels:
            count += 1
    return count

with open('input.txt', 'r') as f:
    text = f.read().lower()

words = text.split()

total_words = len(words)
words_with_more_than_three_vowels = 0
word_counts = {}

for word in words:
    num_vowels = count_vowels(word)
    if num_vowels > 3:
        words_with_more_than_three_vowels += 1

    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

most_frequent_word = min(word_counts, key=lambda k: (-word_counts[k], k))

print("Количество слов в тексте:", total_words)
print("Количество слов, содержащих более трех гласных букв:", words_with_more_than_three_vowels)
print("Слово, которое чаще всего встречается:", most_frequent_word)
