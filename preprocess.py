#replace emoji
#convert the tweet into tokens seperated by words
#remove the words == RT
#remove the words with multiple hash tags or else remove the first hash tag
#this is because 2 hastags might refer to hashtag or some word with character replaced with #
#Or maybe first we can focus on single hashtag
#remove things have @ in beginning

import re
import remove_rt
import remove_notalpha
import spell_correct
import replace_emoji
import regex_clean
import remove_tagging
import expand_contractions
import get_tuples
import lemmatize_fun
from nltk.corpus import stopwords


def preprocess_tweet(tweet):
    stop_words = set(stopwords.words('english'))
    stop_words.remove("not")
    tweet_token_processed=[]
    pos=[]
    tweet_tokens = tweet.split()
    #print(tweet_tokens)
    temp=""
    for i in range(0,len(tweet_tokens)):
        temp=replace_emoji.replace_emoji_fun(tweet_tokens[i])
        temp=expand_contractions.expand_contractions_fun(temp)
        temp=remove_tagging.remove_tagging_fun(temp)
        temp=remove_rt.remove_rt_fun(temp)
        temp=remove_notalpha.remove_notalpha_fun(temp)
        #print(temp)
        c=temp.count('!')
        temp=temp.replace('!',"")
        temp=spell_correct.spell_correct_fun(temp)
        temp=temp.lower()
        temp=temp.split("_")


       # print(temp)

        for j in range(0,len(temp)):
            #print(temp[j])
            if len(temp[j])>1 and regex_clean.regex_clean_fun(temp[j]) and temp[j] not in stop_words:
                tweet_token_processed.append(temp[j])
                if(c):
                    pos.append(len(tweet_token_processed)-1)
    tweet_token_processed = ' '.join(tweet_token_processed)
    tweet_token_processed = lemmatize_fun.lemmatize_fun(tweet_token_processed)
    temp = tweet_token_processed[:]
    tweet_exclamation = []
    for i in range(0, len(pos)):
        #tweet_exclamation.append(tweet_token_processed[pos[i]])
        temp.insert(pos[i]+i,tweet_token_processed[pos[i]])
    temp.extend(get_tuples.get_tuples(temp))
    return temp

#tweet="Dew drops fall from the leaves"
#tweet = 'RT @Daniel no!! no I like Bitcoin!!! impordant!!! 👍 https://bitcoin.com #crypto #dogecoin loo##l loo####l'
#tweet = "Not happy with the way India played... an insipid display of cricket... This side looked like they r on the ground to get beaten..!!!  :'("
#tweet = "I'm soooooo pisssssed"
#tweet = "I do not like it 1002"
#tweet_exclamation=[]
#tweet_token_processed=preprocess_tweet(tweet)
#print(tweet_token_processed)
#print(tweet_exclamation)
#We can remove the stop words, remove the words which are not in dictionary, replace multiple
#puntuation marks with 1
#infact we can also do stemming and lemmatization too
#we can combine all of them i.e one funtion for all of them
#remove the stop words
#stop word might replace not and thus we should use not to replace the next word with antonym
#we can make n-grams here
#stop_words = set(stopwords.words('english'))
#tweet_token_processed=[token for token in tweet_token_processed if not token in stop_words]
#lemmatize starting
#tweet_token_processed=' '.join(tweet_token_processed)
#print(lemmatize_fun.lemmatize_fun(['Mary','leaves', 'the', 'room']))
#tweet_token_processed=lemmatize_fun.lemmatize_fun(tweet_token_processed)
#print(tweet_token_processed)
#tweet_token_processed=tweet_token_processed.split()
#tweet_exclamation=[]
#for i in range(0,len(pos)):
    #tweet_exclamation.append(tweet_token_processed[pos[i]])

#print(tweet_token_processed)
#print(pos)
#print(tweet_exclamation)

#lemmatize ending

#tweet_token_processed.extend(get_tuples.get_tuples(tweet_token_processed))

#print(tweet_token_processed)

