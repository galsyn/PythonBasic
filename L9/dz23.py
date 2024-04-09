def popular_words (text, words):
    my_dict = {}
    for word in words:
        my_dict[word] = my_dict.get(word, 0)
        for el in text.lower().strip().split(" "):
            if el == word:
                my_dict[word] += 1
    return my_dict

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
