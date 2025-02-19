from fastapi import APIRouter, Body, HTTPException
import os
import pickle
import numpy as np
import logging

logging.basicConfig(filename='storage/app.log', level=logging.DEBUG)

router = APIRouter(prefix="/predict", tags=["Prediction"])

# Rutas de modelos predefinidos en /app/models/
model_files = {
    1: "app/models/LogisticRegression_optimized.pkl",
    2: "app/models/DecisionTree_optimized.pkl",
    3: "app/models/RandomForest_optimized.pkl"
}

# Ruta donde se encuentran los modelos de Jupyter
MODEL_DIR = "models"

# Cargar modelos de /models/ automáticamente
def get_dynamic_models():
    dynamic_models = {}
    model_id = max(model_files.keys(), default=0) + 1  # Empezar después del último ID fijo

    if os.path.exists(MODEL_DIR):
        for file in sorted(os.listdir(MODEL_DIR)):
            if file.endswith(".pkl"):
                dynamic_models[model_id] = os.path.join(MODEL_DIR, file)
                model_id += 1  # Incrementar el ID

    return dynamic_models

# Fusionar modelos predefinidos con los nuevos encontrados
def get_all_models():
    all_models = model_files.copy()  # Copiar modelos predefinidos
    all_models.update(get_dynamic_models())  # Agregar modelos detectados dinámicamente
    return all_models

# Función para cargar el modelo según el ID
def load_model(model_id: int):
    model_files_all = get_all_models()
    model_path = model_files_all.get(model_id)
    
    if not model_path:
        raise HTTPException(status_code=404, detail=f"Modelo con id {model_id} no encontrado.")
    
    try:
        with open(model_path, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error cargando el modelo: {str(e)}")

@router.get("/models")
async def list_models():
    """Devuelve una lista de todos los modelos disponibles con su ID y ruta."""
    return get_all_models()

@router.post("/{id}")
async def predict(id: int, features: list = Body(...)):
    """Realiza una predicción usando el modelo seleccionado por ID."""
    model = load_model(id)
    
    try:
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)
    except Exception as e:
        raise HTTPException(status_code=400, detail=f"Error procesando la predicción: {str(e)}")

    logging.info(f"log-prediction: {prediction.tolist()}")
    
    return {"model_id": id, "model_path": get_all_models().get(id), "prediction": prediction.tolist()}
