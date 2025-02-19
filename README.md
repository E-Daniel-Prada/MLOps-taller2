# MLOps-Taller2

Este proyecto contiene un entorno de desarrollo para **Machine Learning** utilizando **Docker Compose**.  
El entorno incluye:
✅ **JupyterLab** para la creación y entrenamiento de modelos.  
✅ **FastAPI** para exponer los modelos como una API de predicción.  
✅ **Carpeta compartida** entre Jupyter y FastAPI para almacenar los modelos entrenados.  

---

##  **Despliegue del Entorno**  

Para iniciar el entorno:  

```sh
docker compose up --build
```
Esto descargará las imágenes necesarias y levantará los contenedores de **JupyterLab** y **FastAPI**.  

Para detener los contenedores en cualquier momento, usa:  

```sh
docker compose down
```

Para reiniciar todo desde cero (eliminando volúmenes y datos), usa:  

```sh
docker compose down -v
```

---

## 📂 **Estructura del Proyecto**  

```
📂 MLOps-Taller2
│── 📂 jupyter_work/              # Directorio donde se guardan los notebooks
│── 📂 models/                    # Carpeta compartida para almacenar los modelos entrenados
│── 📂 app/                        # Carpeta con la API FastAPI
│   ├── 📂 routes/                 # Endpoints de la API
│   │   ├── 📜 predict.py          # Lógica de predicción y carga de modelos
│   ├── 📜 main.py                 # Configuración principal de FastAPI
│── 📜 docker-compose.yml          # Configuración de los servicios en Docker
│── 📜 Dockerfile                  # Configuración de la imagen para FastAPI
│── 📜 requirements.txt            # Dependencias del proyecto
│── 📜 README.md                   # Documentación del proyecto
```

---

##  **Acceso a JupyterLab**  

Una vez que el contenedor está en ejecución, acceder a **JupyterLab** en:  

🔗 **URL de acceso:**  
```
http://localhost:8888
```
El acceso está configurado para **no requerir token ni contraseña**.  

---

##  **Uso de la API de Predicción (FastAPI)**  

La API permite consultar los modelos disponibles y realizar predicciones.  

📌 **Swagger UI (Documentación de la API)**  
Una vez que el servicio esté corriendo:  
🔗 **http://localhost:8989/docs**

---

### 📌 **1️ Consultar los Modelos Disponibles**  
Para ver la lista de modelos cargados en el sistema:

```sh
curl -X GET "http://localhost:8989/predict/models"
```

📌 **Ejemplo de respuesta:**  
```json
{
  "1": "app/models/LogisticRegression_optimized.pkl",
  "2": "app/models/DecisionTree_optimized.pkl",
  "3": "app/models/RandomForest_optimized.pkl",
  "4": "models/Jupyter_LogisticRegression_optimized.pkl",
  "5": "models/Jupyter_DecisionTree_optimized.pkl"
}
```
🔹 Los modelos en `app/models/` son los pre-cargados.  
🔹 Los modelos en `models/` son los generados en **JupyterLab**.  

---

### 📌 **2️⃣ Realizar una Predicción con un Modelo Específico**  

Para hacer una predicción, usa el ID de un modelo y envía los datos de entrada como JSON.  

🔹 **Ejemplo:**  
Si queremos usar el modelo **con ID `4`**, enviamos una solicitud con los datos:  
```sh
curl -X POST "http://localhost:8989/predict/4" -H "Content-Type: application/json" -d "[[47.2, 13.7, 214.0, 4925.0, 1, 2]]"
```

📌 **Ejemplo de Respuesta esperada:**  
```json
{
  "model_id": 4,
  "model_path": "models/Jupyter_DecisionTree_optimized.pkl",
  "prediction": [
    2
  ]
}
```
✅ Esto indica que el modelo fue correctamente cargado y realizó la predicción.  

---


2️⃣ **FastAPI detecta automáticamente los modelos de `models/` y `app/models/`**  
🔹 La API carga modelos desde **ambos directorios** y permite seleccionarlos por ID.  

3️⃣ **consultar `/predict/models` para ver los modelos disponibles**  
🔹 Luego, seleccionas el ID del modelo para hacer una predicción.  

---

##  **Conclusión**  

 **Este entorno permite:**  
✅ Entrenar modelos en **JupyterLab**.  
✅ Compartir los modelos automáticamente con **FastAPI**.  
✅ Realizar predicciones mediante una API.  
