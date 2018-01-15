from sklearn.feature_extraction import DictVectorizer
import csv
from sklearn import tree
from sklearn import preprocessing
from sklearn.externals.six import StringIO

allElectronicsData = open(r'C:\Users\ls\Desktop\exam20180111.csv', 'rt', encoding='utf8', errors='ignore')
reader = csv.reader(allElectronicsData)

featureList = []
labelList = []

# 利用决策树实现分类问题，适用于离散数据
# age    incom  student buy
# youth  high   no      no
# senior high   no      yes
# middle medium yes     yes
#
for index, row in enumerate(reader):
    if index < 105:
        labelList.append(row[5])
        rowDict = {}
        for i in range(1, 5):
            rowDict[i-1] = row[i]
        print("index: " , rowDict)
        featureList.append(rowDict)

vec = DictVectorizer()
dummyX = vec.fit_transform(featureList).toarray()

print("dummyX: " + str(dummyX))
print(vec.get_feature_names())

print("labelList: " + str(labelList))

lb = preprocessing.LabelBinarizer()
dummyY = lb.fit_transform(labelList)
print("dummyY: " + str(dummyY))

clf = tree.DecisionTreeClassifier(criterion='entropy')
clf = clf.fit(dummyX, dummyY)

allElectronicsData = open(r'C:\Users\ls\Desktop\20180111.csv', 'rt', encoding='utf8', errors='ignore')
reader = csv.reader(allElectronicsData)

newRowList = []
for index, row in enumerate(reader):
    if index >= 105:
        newRowX = {}
        for i in range(1, 5):
            newRowX[i-1] = row[i]
        print("newRowX: " , str(newRowX))
        newRowList.append(newRowX)
predictedX = vec.fit_transform(newRowList).toarray()
predictedY = clf.predict(predictedX)
print("predictedY: " + str(predictedY))
print("clf: " + str(clf))





