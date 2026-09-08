import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load dataset (expects StudentsPerformance.csv with headers)
pima = pd.read_csv("StudentsPerformance.csv")

# Use scores as features and predict 'lunch'
feature_cols = ['writing score', 'math score', 'reading score']
X = pima[feature_cols]
y = pima['lunch']

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)

# Train Decision Tree
clf = DecisionTreeClassifier()
clf = clf.fit(X_train, y_train)

# Predict and evaluate
y_pred = clf.predict(X_test)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))

from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image, display

try:
    import pydotplus  # type: ignore[import-not-found]
except ImportError:
    pydotplus = None

if pydotplus is not None:
    dot_data = StringIO()
    export_graphviz(
        clf,
        out_file=dot_data,
        feature_names=feature_cols,
        class_names=clf.classes_.astype(str),
        filled=True,
        rounded=True,
        special_characters=True,
    )
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    display(Image(graph.create_png()))
    input("wait for me..")

