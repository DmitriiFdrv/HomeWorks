# сам совсем не понял
def int_func():
    text = []
    words = input('Введите слова: ')
    new_words = words.capitalize()
    print(new_words)
    return
int_func()
##
#words = input('input smthng: ')
#nwords = words.capitalize()
#print(nwords)
def cap_func(text):
    def int_func(word: str):
        return f'{word[0].upper()}{word[1:]}'
    words = text.split()
    return ''.join(list(map(lambda word: int_func(word), words)))
print(cap_func('test tEDDDY bear beArINg honey'))