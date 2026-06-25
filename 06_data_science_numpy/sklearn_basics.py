"""
Practice: scikit-learn Basics
"""
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def sklearn_demo():
    X = [[1], [2], [3], [4]]
    y = [2, 4, 6, 8]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)

    print(f"Coefficient: {model.coef_[0]:.2f}")
    print(f"Intercept: {model.intercept_:.2f}")
    print(f"Predictions on test: {list(y_pred)}")
    print(f"R^2 score: {model.score(X_test, y_test):.2f}")

if __name__ == "__main__":
    sklearn_demo()
