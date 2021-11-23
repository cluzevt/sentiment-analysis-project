#Here we will take data frame as input. We will create positive-negative dictionary
#then we will create two dimensional data frame and map to corresponding sentiment dataframe
#after that we will split the data into testing and training
#finally we will print the answer
#also we will clean the dataframe by removing the empty list
import pandas as pd
from sklearn.model_selection import  train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

def store_frequency(x,y):
    #we need to get dataframe, where first value correspond to number of positive tweets and
    #second value correspond to number negative tweets in which it occurs
    dict={}
    #print(type(x['1'][0]))
    for i in x.index:
        for token in x['1'][i]:
            if (token,y['0'][i]) not in dict:
                dict[(token,y['0'][i])]=y['0'][i]
            else:
                dict[(token,y['0'][i])]=dict[(token,y['0'][i])]+y['0'][i]
    return dict

def get_dataframe(x,dict):
    df=pd.DataFrame(columns=['0', '1'])
    for i in x.index:
        pos=0
        neg=0
        for token in x['1'][i]:
            if (token,1) in dict:
                pos=pos+dict[(token,1)]
            if (token,-1) in dict:
                neg=neg+dict[(token,-1)]
        df.loc[i]=[pos,-1*neg]
    return df

def solve(df):
    x=df[['1']]
    y=df[['0']]
    #print(y.head(5))
    X_train, X_test, y_train, y_test= train_test_split(x, y, train_size=0.8, random_state=1)

    #print(X_train.head(10))

    #print(X_train.dtypes)
    #print(y_train.dtypes)
    #return

    dict=store_frequency(X_train,y_train)
    X_train=get_dataframe(X_train,dict)
    X_test=get_dataframe(X_test,dict)

    #pd.set_option('display.max_rows', None)
    #result=X_train.head(100)
    #print(result)

    X_train.reset_index(inplace=True, drop=True)
    X_test.reset_index(inplace=True, drop=True)
    y_train.reset_index(inplace=True,drop=True)
    y_test.reset_index(inplace=True,drop=True)

    model=LogisticRegression()
    model.fit(X_train,y_train)
    Y=model.predict(X_test)

    print(y_test)
    print(Y)

    print(confusion_matrix(y_test,Y))
    print(accuracy_score(y_test,Y))





df=pd.read_csv('../dataset_modified_2/data-triplets.csv', encoding='ISO-8859-1',na_filter=True,na_values='[]', converters={'1': pd.eval})
df.dropna(inplace=True)
solve(df)