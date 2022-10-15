'''
5. ** Реализовать функцию, возвращающую n шуток, сформированных из трех случайных слов, взятых из трёх списков (по одному из каждого)
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

in
10 True

out

['дом ночью мягкий', 'огонь завтра зеленый', 'лес вчера яркий', 'автомобиль сегодня веселый', 'город позавчера утопичный']

in
10 False

out

['автомобиль ночью мягкий', 'огонь вчера веселый', 'автомобиль позавчера веселый', 'город вчера утопичный', 'лес сегодня зеленый', 'дом вчера яркий', 'автомобиль вчера зеленый', 'огонь позавчера яркий', 'огонь где-то утопичный', 'автомобиль где-то мягкий']
'''
from random import choices

with open("task_5_words.txt", "r", encoding = "utf-8") as file:
    first_word = file.readline().split()
    second_word = file.readline().split()
    third_word = file.readline().split()
# print(f"{first_word}\n{second_word}\n{third_word}")
    
def create_joke(w1, w2, w3):
    jokes = " ".join(f'{choices(w1)} {choices(w2)} {choices(w3)}\n').replace(",", "")
    print(jokes)


N = int(input("Сколько шуток хотите получить?: "))
for _ in range(N):
    create_joke(first_word, second_word, third_word)