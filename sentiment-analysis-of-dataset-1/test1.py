from sklearn.feature_extraction.text import  TfidfVectorizer
x=[['ab','ab'], ['ab','de']]
vectorizer =TfidfVectorizer(analyzer=lambda x: x)
print(vectorizer.fit_transform(x).toarray())
