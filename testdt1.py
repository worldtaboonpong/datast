import numpy as np
import pandas as pd
from sklearn.tree import DecisionTreeClassifier, export_graphviz
from sklearn import tree
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn import metrics
from IPython.display import SVG
from graphviz import Source
from IPython.display import display

# load dataset
data = load_wine()

df = pd.DataFrame(data.data, columns=data.feature_names)
df.head()

# feature matrix
X = data.data

# target vector
y = data.target

# class labels
labels = data.feature_names

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1) # 70% training and 30% test

# Create Decision Tree classifer object
clf = DecisionTreeClassifier(criterion="entropy", max_depth=None)

# Train Decision Tree Classifer
clf = clf.fit(X_train,y_train)

#Predict the response for test dataset
y_pred = clf.predict(X_test)
y_score = clf.score(X,y)

from sklearn.metrics import classification_report,confusion_matrix

print(classification_report(y_test,y_pred))

graph = Source(export_graphviz(clf, out_file=None,  
                filled=True, rounded=True,
                special_characters=True,feature_names = labels,class_names=['0','1','2']))

display(SVG(graph.pipe(format='svg')))
