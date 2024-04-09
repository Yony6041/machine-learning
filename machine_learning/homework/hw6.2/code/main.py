import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam


def generar_datos_espiral_archimedana_doble(n_puntos, ruido=0.2, vueltas=3):
    """
    Genera un conjunto de datos 2D con dos espirales de Archímedes de un brazo con tres vueltas de 360°,
    cada espiral para una clase diferente.
    """
    # Parámetros para la espiral de Archímedes: r = a + b*theta
    a = 0  # Comenzando en el origen
    b = 1  # Tasa de expansión, asegura una espiral ajustada

    # Generar puntos para el primer brazo de la espiral (Clase 0)
    t = np.linspace(0, 2 * np.pi * vueltas, n_puntos // 2)  # theta
    r = a + b * t  # radio
    x1 = r * np.cos(t) + np.random.randn(n_puntos // 2) * ruido
    y1 = r * np.sin(t) + np.random.randn(n_puntos // 2) * ruido

    # Generar puntos para el segundo brazo de la espiral (Clase 1), rotado 180 grados para diferenciar
    t += np.pi  # desplazar theta 180 grados
    x2 = r * np.cos(t) + np.random.randn(n_puntos // 2) * ruido
    y2 = r * np.sin(t) + np.random.randn(n_puntos // 2) * ruido

    # Combinar x e y en un solo conjunto de datos
    X = np.vstack((np.hstack((x1, x2)), np.hstack((y1, y2)))).T
    y = np.hstack((np.zeros(n_puntos // 2), np.ones(n_puntos // 2)))

    return X, y


# Generar datos de doble espiral
n_puntos = 1000  # Número total de puntos (500 por espiral)
X, y = generar_datos_espiral_archimedana_doble(n_puntos)

# Graficar
plt.scatter(X[y == 0][:, 0], X[y == 0][:, 1], c="orange", label="Clase 0")
plt.scatter(X[y == 1][:, 0], X[y == 1][:, 1], c="blue", label="Clase 1")
plt.title("Datos en Forma de Espiral")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.legend()
plt.show()

# Usar los datos generados previamente (X, y)
# Dividir el conjunto de datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Definir el modelo de keras
modelo = Sequential()
modelo.add(
    Dense(64, input_dim=2, activation="relu")
)  # Primera capa oculta con 64 neuronas y activación ReLU
modelo.add(
    Dense(64, activation="relu")
)  # Segunda capa oculta con 64 neuronas y activación ReLU
modelo.add(
    Dense(1, activation="sigmoid")
)  # Capa de salida con una sola neurona y activación sigmoidal para clasificación binaria

# Compilar el modelo
modelo.compile(
    loss="binary_crossentropy",  # Ya que tenemos un problema de clasificación binaria
    optimizer=Adam(
        learning_rate=0.001
    ),  # Optimizador Adam con una tasa de aprendizaje de 0.001
    metrics=["accuracy"],
)  # La métrica que queremos seguir es la precisión

# Imprimir el resumen del modelo para ver la arquitectura
modelo.summary()

# Entrenar el modelo
historia = modelo.fit(
    X_train,
    y_train,
    validation_split=0.1,  # usar el 10% de los datos de entrenamiento para validación
    epochs=200,  # número de épocas para entrenar
    batch_size=32,
)  # tamaño del lote para el entrenamiento

# Evaluar el modelo
perdida_test, precision_test = modelo.evaluate(X_test, y_test)
print(f"Perdida en prueba: {perdida_test}, Precisión en prueba: {precision_test}")


def graficar_frontera_decision(X, y, modelo):
    # Definir las dimensiones del lienzo
    rango_x = np.linspace(min(X[:, 0]) - 1, max(X[:, 0]) + 1)
    rango_y = np.linspace(min(X[:, 1]) - 1, max(X[:, 1]) + 1)
    xx, yy = np.meshgrid(rango_x, rango_y)
    malla = np.c_[xx.ravel(), yy.ravel()]

    # Hacer predicciones a través de la malla
    func_pred = modelo.predict(malla)
    z = func_pred.reshape(xx.shape)

    # Graficar el contorno y los ejemplos de entrenamiento
    plt.contourf(xx, yy, z, cmap="RdBu", alpha=0.5)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap="RdBu", lw=0)
    plt.title("Frontera de Decisión")
    plt.xlabel("Característica 1")
    plt.ylabel("Característica 2")


# Graficar la frontera de decisión
graficar_frontera_decision(X, y, modelo)
plt.show()
