def remove_rt_fun(tweet_token):
    if(tweet_token=="RT"):
        return "1"
    else:
        return tweet_token