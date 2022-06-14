def f(string):
    y = ''
    i = 0
    for x in string:
        y += x.lower() if i else x.upper()
        if x != ' ':
            i = 1 - i
    return y


string = ''

