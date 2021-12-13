import string
def percent(words):
    words_percents = []
    for i in words:
        percent = round(100*words.count(i)/len(words), 2)
        words_percents.append(percent)
    return words_percents
def text_analysis(text):
    with open(text, 'r', encoding='utf-8') as text:
        t = text.read()
    t = t.lower().translate(t.maketrans('—', ' ', string.punctuation)).split()
    set_t = set(t)
    longest_word = max(set_t, key=len)
    longest_words = set([i for i in t if len(i) == len(longest_word)])
    words_freq = percent(t)
    max_percent = max(words_freq)
    max_freq_words = set([i for i in t if words_freq[t.index(i)] == max_percent])
    lw = ''
    for i in longest_words:
        lw += i
    mfw = ''
    for i in max_freq_words:
        mfw += i
    return lw, mfw
with open('text3.txt', 'w+', encoding='utf-8') as text:
    lines = '''Варкалось. Хливкие шорьки Пырялись по наве, И хрюкотали зелюки, Как мюмзики в мове.
О, бойся Бармаглота, сын! Он так свирлеп и дик! А в глу́ше ры́мит исполин — Злопастный Брандашмыг!
Но взял он меч, и взял он щит, Высоких полон дум. В глущобу путь его лежит Под дерево Тумтум.
Он стал под дерево и ждёт. И вдруг граахнул гром — Летит ужасный Бармаглот И пылкает огнём!
Раз-два, раз-два! Горит трава, Взы-взы — стрижает меч, Ува! Ува! И голова Барабардает с плеч!
О светозарный мальчик мой! Ты победил в бою! О храброславленный герой, Хвалу тебе пою!
Варкалось. Хливкие шорьки Пырялись по наве. И хрюкотали зелюки, Как мюмзики в мове.'''

    text.write(lines)
with open('text3.txt', 'r', encoding='utf-8') as text:
    t = text.read()
print(t)
result = text_analysis('text3.txt')
print(f'Самое длинное слово: {result[0]}\nСамое частое слово: {result[-1]}')