def correct_sentence(text):
    new_text = text.replace(text[0], text[0].upper(), 1)
    if text[-1] != '.':
        new_text = text.replace(text[0], text[0].upper(), 1) + "."
    return new_text

assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print('ОК')
