# Importamos las herramientas necesarias
from sklearn.neural_network import MLPClassifier
import numpy as np

# Datos de entrada (X): [Edad, Ingresos_Mensuales, Deuda_Actual]
X = np.array([
    [25, 2000, 500],
    [45, 5000, 1000],
    [30, 1500, 2000],
    [50, 8000, 500]
])

# Datos de salida (y): 1 = Crédito Aprobado, 0 = Crédito Rechazado
y = np.array([1, 1, 0, 1])

# Creamos la Red Neuronal (Perceptrón Multicapa)
# hidden_layer_sizes=(5, 2) significa 2 capas ocultas con 5 y 2 neuronas respectivamente
red_neuronal = MLPClassifier(hidden_layer_sizes=(5, 2), max_iter=1000, random_state=42)

# Entrenamos el modelo con nuestros datos
red_neuronal.fit(X, y)

# Realizamos una predicción para un nuevo cliente: 35 años, $3000 de ingresos, $800 de deuda
nuevo_cliente = np.array([[35, 3000, 800]])
prediccion = red_neuronal.predict(nuevo_cliente)

if prediccion[0] == 1:
    print("Resultado: Crédito Aprobado")
else:
    print("Resultado: Crédito Rechazado")