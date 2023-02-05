words_input = input('Input text: ').split(' ')


def search_letter(list_of_search):
    letters: list = []
    for word in list_of_search:
        letters.append(search_first_letter(word))
    return letters


def search_first_letter(world_of_search):
    letter: str = ''
    for letter in world_of_search:
        tmp = world_of_search.count(letter)
        if tmp == 1:
            break
    return letter

print('Answer: ' + search_first_letter(search_letter(words_input)))
