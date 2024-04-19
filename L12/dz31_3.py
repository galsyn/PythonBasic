import codecs


def txt_from_html(html):
    while html.find("<") != -1:
        x1 = html.find("<")
        x2 = html.find(">")
        html = html.replace(html[x1:x2 + 1], "")
    new_lst = html.split("\n")
    new_ = list(filter(lambda x: x.strip(), new_lst))
    return  '\n'.join(new_)


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        file.close()

    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(txt_from_html(html))
        file.close()


delete_html_tags('draft.html', 'prob3.txt')
