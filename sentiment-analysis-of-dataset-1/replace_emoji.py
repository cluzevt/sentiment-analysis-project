import emoji

def replace_emoji_fun(token):
    return emoji.demojize(token, delimiters=("", ""))
