def make_prediction(model, X_new):
    """Realiza una predicción usando el modelo entrenado."""
    prediction = model.predict(X_new)
    return prediction
