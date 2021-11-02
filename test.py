def convert(lst):
    return str(lst).translate(None, '[],\'')


# Driver code
lst = ['geeks', 'for', 'geeks']
print(convert(lst))