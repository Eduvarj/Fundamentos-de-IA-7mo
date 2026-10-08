"""
Prototipo funcional minimo: Red Neuronal para reconocer digitos escritos a mano.

Caso de uso real: este mismo principio es el que usan los bancos y el correo
postal para leer automaticamente numeros escritos a mano (OCR) en cheques,
formularios y sobres.

Como correrlo:
    pip install scikit-learn matplotlib --break-system-packages   (si hace falta)
    python3 prototipo_red_neuronal.py

Que hace, linea por linea (para que el equipo lo pueda explicar):
"""

# 1. Herramientas: sklearn trae el dataset y la red neuronal ya lista.
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
import matplotlib.pyplot as plt

# 2. DATOS DE ENTRADA: 1797 imagenes de digitos (0-9), cada una de 8x8 pixeles.
#    "X" es la entrada: cada imagen se aplana a un vector de 64 numeros
#    (el nivel de gris de cada pixel). "y" es la etiqueta correcta (0 al 9).
digitos = load_digits()
X, y = digitos.data, digitos.target
print(f"Numero de ejemplos: {X.shape[0]}  |  Numero de pixeles por imagen: {X.shape[1]}")

# 3. Separamos los datos: 80% para ENTRENAR la red, 20% para EVALUARLA
#    con ejemplos que nunca vio (asi sabemos si de verdad aprendio).
X_entrena, X_prueba, y_entrena, y_prueba = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Escalamos los valores (0-16 de gris) a una escala estandar.
#    Las redes neuronales aprenden mejor y mas rapido con datos escalados.
escalador = StandardScaler()
X_entrena = escalador.fit_transform(X_entrena)
X_prueba = escalador.transform(X_prueba)

# 5. LA RED NEURONAL:
#    - hidden_layer_sizes=(32,) -> una sola capa oculta con 32 "neuronas"
#    - activation='relu'        -> funcion de activacion de cada neurona
#    - max_iter=300             -> hasta 300 pasadas de aprendizaje (epocas)
#    - random_state=42          -> para que el resultado sea reproducible
red = MLPClassifier(
    hidden_layer_sizes=(32,),
    activation="relu",
    max_iter=300,
    random_state=42,
)

# 6. ENTRENAMIENTO: aqui la red ajusta sus pesos internos viendo miles de
#    ejemplos correctos, hasta aprender a distinguir un digito de otro.
red.fit(X_entrena, y_entrena)

# 7. SALIDA / PREDICCION: le damos imagenes que nunca vio y le pedimos
#    que adivine que digito es cada una.
predicciones = red.predict(X_prueba)

# 8. RESULTADOS OBSERVABLES (para el rol de QA del equipo):
exactitud = accuracy_score(y_prueba, predicciones)
print(f"\nExactitud del modelo: {exactitud * 100:.2f}%")
print("\nReporte de clasificacion por digito:")
print(classification_report(y_prueba, predicciones))

# 9. MATRIZ DE CONFUSION: muestra en que digitos se equivoca mas la red.
matriz = confusion_matrix(y_prueba, predicciones)
plt.figure(figsize=(6, 5))
plt.imshow(matriz, cmap="Blues")
plt.title("Matriz de confusion - Reconocimiento de digitos")
plt.xlabel("Digito predicho")
plt.ylabel("Digito real")
plt.colorbar()
for i in range(10):
    for j in range(10):
        plt.text(j, i, matriz[i, j], ha="center", va="center", fontsize=8)
plt.tight_layout()
plt.savefig("matriz_confusion.png", dpi=200)
print("\nSe guardo la imagen 'matriz_confusion.png' con los resultados.")

# 10. DEMO VISUAL: mostramos 8 ejemplos reales con la prediccion de la red.
fig, ejes = plt.subplots(2, 4, figsize=(10, 5))
for ax, imagen, real, pred in zip(
    ejes.ravel(), X_prueba[:9], y_prueba[:9], predicciones[:9]
):
    ax.imshow(imagen.reshape(8, 8), cmap="gray_r")
    color = "green" if real == pred else "red"
    ax.set_title(f"Real: {real} | Prediccion: {pred}", color=color, fontsize=10)
    ax.axis("off")
plt.suptitle("Ejemplos de prediccion de la red neuronal")
plt.tight_layout()
plt.savefig("ejemplos_prediccion.png", dpi=200)
print("Se guardo la imagen 'ejemplos_prediccion.png' con ejemplos de la demo.")