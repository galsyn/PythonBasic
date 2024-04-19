import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        file.close()
    while html.find("<") != -1:
        x1 = html.find("<")
        x2 = html.find(">")
        html = html.replace(html[x1:x2 + 1], "")
    html = html.strip("")
    with codecs.open(result_file, 'w', 'utf-8') as file:
        file.write(html)
        file.close()


delete_html_tags('draft.html', 'prob1.txt')
