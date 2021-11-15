#if token has more than two hashtag then skip it, else remove those two hashtags and return
#the word
import re
def remove_notalpha_fun(token):
    if "//" in token:
        return "1"
    else:
        return re.sub("[^a-zA-Z!_]+","",token)