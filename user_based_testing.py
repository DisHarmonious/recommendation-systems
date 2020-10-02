import pandas as pd
import numpy as np
import os
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.utils import shuffle
from sklearn import preprocessing
from sklearn import linear_model
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import MultinomialNB
from sklearn.naive_bayes import BernoulliNB
import random

os.chdir("C:\\Users\\user\\Desktop\\kalder")
dataset=pd.read_csv(r'rated.csv', sep=" ", header=None)
dataset=shuffle(dataset)

X=dataset.iloc[:,0:9]


X['r1']=[random.random() for i in range(0,len(dataset))]
X['r2']=[random.random() for i in range(0,len(dataset))]
X['r3']=[random.random() for i in range(0,len(dataset))]
X['r4']=[random.random() for i in range(0,len(dataset))]
X['r5']=[random.random() for i in range(0,len(dataset))]
X['r6']=[random.random() for i in range(0,len(dataset))]
X['r7']=[random.random() for i in range(0,len(dataset))]
X['r8']=[random.random() for i in range(0,len(dataset))]
X['r9']=[random.random() for i in range(0,len(dataset))]
X['r10']=[random.random() for i in range(0,len(dataset))]


'''
X['ac1']=np.ones(len(dataset))
X['ac2']=np.ones(len(dataset))
X['ac3']=np.ones(len(dataset))
X['ac4']=np.ones(len(dataset))
X['ac5']=np.ones(len(dataset))
X['ac6']=np.ones(len(dataset))
X['ac7']=np.ones(len(dataset))
X['ac8']=np.ones(len(dataset))
X['ac9']=np.ones(len(dataset))
X['ac10']=np.ones(len(dataset))
X['ac11']=np.ones(len(dataset))
X['ac12']=np.ones(len(dataset))
X['ac13']=np.ones(len(dataset))
X['ac14']=np.ones(len(dataset))
X['ac15']=np.ones(len(dataset))
X['ac16']=np.ones(len(dataset))
X['ac17']=np.ones(len(dataset))
X['ac18']=np.ones(len(dataset))
X['ac19']=np.ones(len(dataset))
X['ac20']=np.ones(len(dataset))
'''

Y=dataset.iloc[:,9]

x_train=X.iloc[0:6001,:]
x_test=X.iloc[6000:,:]
y_train=Y.iloc[0:6001]
y_test=Y.iloc[6000:]

'''
clf = BernoulliNB().fit(x_train, y_train)
a=clf.score(x_test, y_test)
print(a)
'''

'''
clf = MultinomialNB().fit(x_train, y_train)
a=clf.score(x_test, y_test)
print(a)
'''

'''
clf = MLPClassifier(learning_rate='adaptive').fit(x_train, y_train)
a=clf.score(x_test, y_test)
print(a)
'''

'''
clf = LogisticRegression(max_iter=10000,random_state=0).fit(x_train, y_train)
a=clf.score(x_test, y_test)
print(a)
'''

'''
clf = linear_model.BayesianRidge().fit(x_train, y_train)
a=clf.score(x_test, y_test)
print(a)
'''


clf = RandomForestClassifier(max_depth=10, random_state=0, n_estimators=1000).fit(x_train, y_train)
a=clf.score(x_test, y_test)
print(a)



#predict probabilities of belonging to a class
probs = clf.predict_proba(x_test)
n=5
best_n = np.argsort(probs, axis=1)[:,-n:]

print(best_n)

#update weight vector
#update=clf.partial_fit(x_test[0],y_test[0])



