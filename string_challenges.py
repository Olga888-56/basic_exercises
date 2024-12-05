# Вывести последнюю букву в слове
word = 'Архангельск'
last = word[-1]
print(last)
# ???


# Вывести количество букв "а" в слове
word = 'Архангельск'
a= word.lower()
print(a.count('а'))
# ???


# Вывести количество гласных букв в слове
word = 'Архангельск'
vowels = "аеёиоуыэюяАЕЁОИУЫЭЮЯ"
count_vow = 0
for letter in word.lower():
    if letter in vowels:
        count_vow += 1

print(count_vow)

# ???


# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
num_words = len(words)
print(num_words)
# ???


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
words = sentence.split()
for word in words:
    print(word[0])
# ???


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
words = sentence.split()
num_words = len(words)
for word in words:
    avg_word_len = len(sentence) / num_words
print(f"Средняя длина слова в предложении {avg_word_len}")
# ???