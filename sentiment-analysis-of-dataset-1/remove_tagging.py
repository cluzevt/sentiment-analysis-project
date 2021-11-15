def remove_tagging_fun(token):
    if len(token)>0 and token[0]=='@':
        return "1"
    else:
        return token