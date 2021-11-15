from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
from cuml import svm
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from ast import literal_eval
import cudf


def solve(x, y):
    X_train, X_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=1)

    # print(X_train.head(10)
    # pd.set_option('display.max_rows', None)
    # result=X_train.head(100)
    # print(result)
    # print(X_train.head(2))
    # print(y_train.head(2))
    # print(X_train.dtypes)
    # print(y_train.dtypes)
    # return

    X_train.reset_index(inplace=True, drop=True)
    X_test.reset_index(inplace=True, drop=True)
    y_train.reset_index(inplace=True, drop=True)
    y_test.reset_index(inplace=True, drop=True)

    # model = LogisticRegression()
    model = svm.SVC()
    model.fit(X_train, y_train)
    Y = model.predict(X_test)

    # Y=Y.astype('int32')
    # y_test=y_test.astype('int32')

    # Y=Y.to_arrow().to_pylist()

    # y=y.tolist()
    print(type(Y))
    print(type(y_test))

    Y = Y.to_arrow().to_pylist()
    y_test = y_test.to_pandas()

    print("we are here")

    print(confusion_matrix(y_test, Y))
    print(accuracy_score(y_test, Y))

cudf.set_allocator("managed")
# df=pd.read_csv('sa_file_processed1.csv', encoding='ISO-8859-1',na_filter=True,na_values='[]', converters={'1': pd.eval})
df = pd.read_csv('sa_file_processed1.csv', encoding='ISO-8859-1', na_filter=True, na_values='[]',
                 converters={"1": literal_eval})
df.dropna(inplace=True)
df = df.head(14000)
vectorizer = CountVectorizer(analyzer=lambda x: x)
# arr=vectorizer.fit_transform(df['1'].tolist()).toarray()
# lis=[]
# for e in arr:
#   lis.append(e.tolist())
# df['1']=lis
arr = vectorizer.fit_transform(df['1'].tolist())
# print(arr)
# print(vectorizer.get_feature_names())
x = pd.DataFrame(arr.todense(), columns=vectorizer.get_feature_names())

df['0'].loc[(df['0'] == -1)] = 0
df['0'].loc[(df['0'] == 1)] = 1

y = df[['0']]

cols = x.columns
x[cols] = x[cols].apply(pd.to_numeric, errors='coerce')

cols = y.columns
y[cols] = y[cols].apply(pd.to_numeric, errors='coerce')

x = cudf.DataFrame.from_pandas(x).astype('float64')
y = cudf.DataFrame.from_pandas(y).astype('float64')

# x=x.astype('float64')
# y=y.astype('float64')
# print(x.head(2))

print("toward solving")
solve(x, y)