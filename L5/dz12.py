import string

# my_str = 'Python Community'
# my_str = 'i like python community!'
my_str = ' Should, I. subscribe? Yes! '
my_str = my_str.title()
for sign_ in string.punctuation:
    if sign_ in my_str:
        my_str = my_str.replace(sign_, '')
lst = my_str.split()
my_str = "#" + "".join(lst)
hash_str = my_str[:138]
print(hash_str)
