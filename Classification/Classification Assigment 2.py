import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

col_names=['Item_Identifier','Item_Fat','Item_Type','Item_Visibility']
#load dataset
pima=pd.read_csv("Train.csv", header=0, names=col_names)
print(pima.columns)
feature_cols = ['Item_Identifier', 'Item_Type', 'Item_Visibility']

target_col = 'Item_Fat'

X = pima[feature_cols]
y = pima[target_col]

# Text ko numbers mein convert karna
X = pd.get_dummies(X)
y = pd.factorize(y)[0]

# Data split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Decision Tree
clf = DecisionTreeClassifier()

# Train
clf.fit(X_train, y_train)

# Prediction
y_pred = clf.predict(X_test)

# Accuracy
print("Accuracy:", clf.score(X_test, y_test))

# Model Accuracy, how often is the classifier correct?
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))

from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus

dot_data = StringIO()
export_graphviz(
    clf,
    out_file=dot_data,
    filled=True,
    rounded=True,
    special_characters=True,
    feature_names=X.columns,
)

graph=pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_png('diabetev1.png')
Image(graph.create_png())

""""Well, the classification rate increased to 77.05%, which is better accuracy than the previous model."""


from six import StringIO 
from IPython.display import Image  
from sklearn.tree import export_graphviz
import pydotplus
dot_data = StringIO()
export_graphviz(
    clf,
    out_file=dot_data,
    filled=True,
    rounded=True,
    special_characters=True,
    feature_names=X.columns
)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())  
graph.write_png('diabetev3.png')
Image(graph.create_png())


input("Wait for me...")