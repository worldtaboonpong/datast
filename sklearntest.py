from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics

iris = datasets.load_iris()

print(iris.DESCR)
print(iris.data)
model = KNeighborsClassifier()
model.fit(iris.data, iris.target)
pred = model.predict(iris.data)
print(metrics.classification_report(iris.target, pred))