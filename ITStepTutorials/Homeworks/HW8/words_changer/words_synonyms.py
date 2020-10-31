# 2. Взять любой текст (к примеру с https://yandex.ru/referats/). К домашнему заданию есть 
# приложенный файл synonyms-base.csv, создать 2 версий данного текста, используя базу синонимов.
import re
import csv
from random import randint


example_text = '''
Продвижение проекта самопроизвольно. Слово, в первом приближении, доказывает департамент маркетинга и продаж,
учитывая результат предыдущих медиа-кампаний. Политическая легитимность символизирует скрытый смысл, 
что получило отражение в трудах Михельса. Кроме того, постоянно воспроизводится постулат о письме как о технике, 
обслуживающей язык, поэтому аффилиация изящно отражает гуманизм, размещаясь во всех медиа. Легитимность власти возможна.

Палимпсест ограничивает марксизм, осознав маркетинг как часть производства. Иными словами, понятие тоталитаризма 
тормозит контрапункт. Скрытый смысл аннигилирует культурный ритм. Анализ состава 17 рукописных сборников, 
содержащих тексты стихотворных фацеций, позволяет сделать вывод о том, что торговая марка нейтрализует 
конкретный элемент политического процесса. Согласно последним исследованиям, product placement аннигилирует 
институциональный мониторинг активности. Различное расположение, с другой стороны, изменяет социализм.

Глобализация, с другой стороны, аллитерирует сюжетный либерализм. Борьба демократических и олигархических 
тенденций существенно представляет собой строфоид, о чем будет подробнее сказано ниже. Политический процесс 
в современной России, как правило, версифицирован. Ассортиментная политика предприятия, в первом приближении, 
просветляет системный анализ. Поэтика, несмотря на внешние воздействия, отражает медиабизнес. Возможно 
денотативное тождество языковых единиц при их сигнификативном различии, например, политическое лидерство нетривиально.
'''
text_version1 = ''
text_version2 = ''

# !!! Change this path to your own !!!
path_to_file = 'ITStepTutorials\\Homeworks\\HW8\\words_changer\\'

dictionary_syn = {}
with open(path_to_file + 'synonyms-base.csv', mode='r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, dialect='excel')
    for synonyms in reader:
        letter = synonyms[0][0]
        tuple_synonyms = tuple(synonyms)

        if dictionary_syn.get(letter) == None:
            dictionary_syn[letter] = [ tuple_synonyms ]
        else:
            dictionary_syn[letter].append(tuple_synonyms)

# print(dictionary_syn)

def get_similar_text(text: str) -> str:
    # result = ''
    
    word_pattern = re.compile(r'\w{2,}')
    words_list = word_pattern.findall(text)

    for word in words_list:
        sim_letter_list = dictionary_syn.get(word[0].lower())
        if sim_letter_list is not None:
            new_word = word
            for syns_tuple in sim_letter_list:
                if word.lower() in syns_tuple:
                    new_word = (syns_tuple[randint(0, len(syns_tuple) - 1)] + ' ').strip()
                    break
            if word.istitle():
                text = text.replace(word, new_word.capitalize())
            else:
                text = text.replace(word, new_word)

    return text


# Results
text_version1 = get_similar_text(example_text)
print('First text:\n',text_version1)

text_version2 = get_similar_text(example_text)
print('Second text:\n', text_version2)
