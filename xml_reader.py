from pprint import pprint
import xml.etree.ElementTree as ET



file_name = 'newsafr.xml'

mytree = ET.parse(file_name)
myroot = mytree.getroot()
channel = myroot[0]


##########################################################
def find_six_and_more(list):
    """находим слова длиннее 6-ти символов"""
    lst_to_return = []

    for i in list:
        if len(i) > 6:
            lst_to_return.append(i.lower())

    return lst_to_return



def return_top_ten(list):
    """возвращаем топ 10 слов"""
    word = ''
    lst = []

    for i in range (10):
        max = 0

        for i in list:
            count = list.count(i)
            if count > max and i not in lst:
                max = count
                word = i

        lst.append(word)
        print(f'{word}   :   встречается {max} раз')
##########################################################


words_lst = []
for item in channel.findall('item'):
    description = item[2].text

    for i in description.split():
        words_lst.append(i)



six_and_more_list = find_six_and_more(words_lst)
return_top_ten(six_and_more_list)