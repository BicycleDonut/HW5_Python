# 1. Напишите программу, удаляющую из текста все слова, содержащие "абв".
#    В тексте используется разделитель пробел.

#in
#Number of words: 10

#out
#авб абв бав абв вба бав вба абв абв абв
#авб бав вба бав вба

from random import sample


def col_rand_words(count: int, alp: str = 'абв'):
    words_col = []
    for i in range(count):
        letters = sample(alp, 3)
        words_col.append("".join(letters))
    return " ".join(words_col)

def simple_sentence(words: str) -> str:
    return " ".join(words.replace("абв", "").split())

all_list = col_rand_words(int(input("Number of words: ")))
print(all_list)
print(simple_sentence(all_list))