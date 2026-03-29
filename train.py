from sklearn.tree import DecisionTreeClassifier

# Sample dataset: [length, concept_count]
X = [
    [2, 1],
    [3, 1],
    [4, 2],
    [5, 2],
    [6, 3],
    [7, 3]
]

# Labels
y = ["Easy", "Easy", "Medium", "Medium", "Hard", "Hard"]

model = DecisionTreeClassifier()
model.fit(X, y)


def get_model():
    return model