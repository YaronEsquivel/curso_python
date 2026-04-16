import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

df = pd.read_csv("src/app/data.csv")

df = df.dropna()

X = df[["edad", "salario", "genero"]]
y = df["comprado"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = RandomForestClassifier()

model.fit(X_train, y_train)

preds = model.predict(X_test)
print("accuracy:", accuracy_score(y_test, preds))

joblib.dump(model, "model.pkl")

print("modelo guardado")
