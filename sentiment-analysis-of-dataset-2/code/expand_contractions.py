import contractions
def expand_contractions_fun(token):
    return contractions.fix(token)

#print(expand_contractions_fun("won't"))