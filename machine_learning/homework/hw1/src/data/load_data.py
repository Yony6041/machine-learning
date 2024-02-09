import pandas as pd


def load_and_preprocess_data(filepath):
    """Carga los datos y calcula estadísticas descriptivas."""
    data = pd.read_csv(filepath)

    # Calcula las estadísticas descriptivas para las horas dedicadas
    horas_stats = data["horas"].describe()
    print("Estadísticas de Horas Dedicadas:")
    print(horas_stats)

    # Calcula las estadísticas descriptivas para las calificaciones
    calificaciones_stats = data["calificaciones"].describe()
    print("\nEstadísticas de Calificaciones:")
    print(calificaciones_stats)

    # Retorna el DataFrame por si se necesita para operaciones futuras
    return data


# Asegúrate de ajustar la ruta al archivo 'datos.csv' según tu estructura de directorio
if __name__ == "__main__":
    load_and_preprocess_data("ruta/a/datos.csv")
