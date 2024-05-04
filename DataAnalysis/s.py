# from sklearn.ensemble import RandomForestClassifier
# clf = RandomForestClassifier(random_state=0)
# X = [[ 1,  2,  3],  # 2 samples, 3 features
#      [11, 12, 13]]
# y = [0, 1]  # classes of each sample
# clf.fit(X, y)

# from sklearn.preprocessing import StandardScaler
# X = [[0, 15],
#      [1, -10]]
# # scale data according to computed scaling values
# StandardScaler().fit(X).transform(X)

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import make_pipeline
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
# create a pipeline object
pipe = make_pipeline(
    StandardScaler(),
    LogisticRegression()
)
# load the iris dataset and split it into train and test sets
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)
# fit the whole pipeline
pipe.fit(X_train, y_train)
# we can now use it like any other estimator
accuracy_score(pipe.predict(X_test), y_test)