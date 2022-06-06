text = '''
'''
from collections import Counter
text_list = text.split()

print(text_list)
text_list.sort(key=Counter(text_list).get)
word_list = list()
for word in text_list:
    word_list.append(word)
    if word_list.count(word) == 1 and len(word)>2:
        print(f'"{word}" appears {text.count(word)} time(s)')








