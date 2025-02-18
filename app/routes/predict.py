from fastapi import APIRouter, Body, HTTPException
import pickle
import numpy as np
import logging

logging.basicConfig(filename='storage/app.log', level=logging.DEBUG)

router = APIRouter(prefix="/predict", tags=["Prediction"])

# Diccionario que mapea IDs a nombres de archivos de modelos
model_files = {
    1: "app/models/LogisticRegression_optimized.pkl",
    2: "app/models/DecisionTree_optimized.pkl",
    3: "app/models/RandomForest_optimized.pkl"
}

# Función para cargar el modelo según el ID
def load_model(model_id: int):
    model_path = model_files.get(model_id)
    if not model_path:
        raise HTTPException(status_code=404, detail=f"Modelo con id {model_id} no encontrado.")
    with open(model_path, "rb") as f:
        return pickle.load(f)

@router.post("/{id}")
async def predict(id: int, features: list = Body(...)):
    model = load_model(id)
    prediction = model.predict(np.array(features).reshape(1, -1))

    logging.info(f"log-prediction: {prediction.tolist()}")

    return {"model_id": model_files.get(id), "prediction": prediction.tolist()}
