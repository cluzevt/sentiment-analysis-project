from pywsd.utils import lemmatize_sentence
def lemmatize_fun(token_list):
    return lemmatize_sentence(token_list)

#print("Here")
#print(lemmatize_fun("Mary leaves the room"))