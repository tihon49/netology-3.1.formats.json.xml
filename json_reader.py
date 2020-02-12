import json
from pprint import pprint



file_name = 'newsafr.json'


def find_six_and_more():
    """находим слова длиннее 6-ти символов"""
    six_more_lst = []

    for news in file['rss']['channel']['items']:
        # title = news['title']
        # date = news['pubDate']
        description = news['description']

        for i in description.split():
            if len(i) > 6:
                six_more_lst.append(i.lower())

        # print(f'Дата: {date}')
        # print(title + '\n')
        # print(description + '\n\n')
    return six_more_lst



def return_top_ten(list):
    """возвращаем топ 10 слов"""
    word = ''
    lst = []

    for i in range (10):
        max = 0

        for i in list:
            count = list.count(i)
            if count > max:
                max = count
                word = i

        # lst.append ([word, max])
        lst.append(word)

        for i in list:
            if i == word:
                list.remove (i)
    return lst



with open(file_name, encoding='utf-8') as f:
    file = json.load(f)
    six_more_list = find_six_and_more()
    top_ten = return_top_ten(six_more_list)

    pprint(top_ten)