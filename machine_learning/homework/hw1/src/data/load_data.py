import pandas as pd


def load_and_preprocess_data(filepath):
    """Carga y realiza un preprocesamiento básico de los datos."""
    data = pd.read_csv(filepath)
    return data
