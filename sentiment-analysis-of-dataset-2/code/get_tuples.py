from nltk import ngrams
def get_tuples(tweet_list):
    lis=[]
    for n in range(2,2):
        sixgrams = ngrams(tweet_list, n)
        for grams in sixgrams:
            tempstr=""
            for token in grams:
                tempstr=tempstr+"_"+token
            lis.append(tempstr)
    return lis

