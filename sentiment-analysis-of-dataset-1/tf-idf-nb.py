from sklearn.feature_extraction.text import  TfidfVectorizer
import pandas as pd
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import  MultinomialNB
from sklearn.model_selection import train_test_split
from ast import literal_eval

def solve(x,y):
    X_train, X_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=1)

    # print(X_train.head(10)
    # pd.set_option('display.max_rows', None)
    # result=X_train.head(100)
    # print(result)
    #print(X_train.head(2))
    #print(y_train.head(2))
    #print(X_train.dtypes)
    #print(y_train.dtypes)
    #return

    X_train.reset_index(inplace=True, drop=True)
    X_test.reset_index(inplace=True, drop=True)
    y_train.reset_index(inplace=True, drop=True)
    y_test.reset_index(inplace=True, drop=True)

    #model = LogisticRegression()
    model=MultinomialNB()
    model.fit(X_train, y_train)
    Y = model.predict(X_test)


    print(confusion_matrix(y_test, Y))
    print(accuracy_score(y_test, Y))


df=pd.read_csv('sa_file_processed1.csv', encoding='ISO-8859-1',na_filter=True,na_values='[]', converters={"1": literal_eval})
df.dropna(inplace=True)
vectorizer = TfidfVectorizer(analyzer=lambda x:x)
#arr=vectorizer.fit_transform(df['1'].tolist()).toarray()
#lis=[]
#for e in arr:
 #   lis.append(e.tolist())
#df['1']=lis
arr=vectorizer.fit_transform(df['1'].tolist())
#print(arr)
#print(vectorizer.get_feature_names())
x = pd.DataFrame(arr.todense(), columns=vectorizer.get_feature_names())

#print(x.head(2))

solve(x,df['0'])