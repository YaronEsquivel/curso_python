import joblib
import pandas as pd

model = joblib.load("model.pkl")

nuevo_usuario = [[30, 38000, 0]]

nuevo_usuario_2 = pd.DataFrame([{"edad": 35, "salario": 43000, "genero": 1}])

pred = model.predict(nuevo_usuario)

print("predicción 1:", pred[0])

pred = model.predict(nuevo_usuario_2)

print("predicción 2:", pred[0])
