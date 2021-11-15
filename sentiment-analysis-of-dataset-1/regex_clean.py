import re
def regex_clean_fun(token):
    pattern = re.compile(r'^[a-z]+!*$')
    temp=pattern.search(token)
    return temp!=None and temp.group()==token
