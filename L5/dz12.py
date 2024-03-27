import string

# my_str = 'Python Community'
# my_str = 'i like python community!'
# my_str = ' Should, I. subscribe? Yes! '
my_str = input('Input your string: ')
my_str = my_str.title()
for sign_ in string.punctuation:
    if sign_ in my_str:
        my_str = my_str.replace(sign_, '')
my_str = "#" + "".join(my_str.split())
hash_str = my_str[:140]
print(hash_str)
