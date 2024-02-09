import matplotlib.pyplot as plt


def plot_regression_line(X, y, model):
    """Grafica los datos y la línea de regresión."""
    plt.scatter(X, y, color="blue")
    plt.plot(X, model.predict(X), color="red", linewidth=2)
    plt.title("Regresión Lineal")
    plt.xlabel("X")
    plt.ylabel("y")
    plt.show()
