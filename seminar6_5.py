from random import choice


def get_jokes(num, uniq, list_1, list_2, list_3):
    if uniq is False:
        for i in range(num):
            print(f"{choice(list_1)} {choice(list_2)} {choice(list_3)}")
    else:
        if num > len(list_1) or num > len(list_2) or num > len(list_3):
            print(f"You can't come up with so many jokes")
        else:
            for i in range(num):
                word_1 = choice(list_1)
                list_1.remove(word_1)
                word_2 = choice(list_2)
                list_2.remove(word_2)
                word_3 = choice(list_3)
                list_3.remove(word_3)
                print(f"{word_1} {word_2} {word_3}")


nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "когда-то", "где-то"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
get_jokes(int(input("Введите количество шуток: ")), True, nouns, adverbs, adjectives)
