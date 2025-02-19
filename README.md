# MLOps-taller2

Este proyecto contiene un entorno de desarrollo para **Machine Learning** utilizando **Docker Compose**.  
El entorno incluye **JupyterLab** para la creación y entrenamiento de modelos de aprendizaje automático.


## Despliegue del Entorno

Para iniciar el entorno, abre una terminal en la carpeta del proyecto y ejecuta:

```sh
docker compose up --build
```

Esto descargará las imágenes necesarias y levantará los contenedores de **JupyterLab**.

detener los contenedores en cualquier momento, usa:

```sh
docker compose down
```

reiniciar todo desde cero (eliminando volúmenes y datos), usa:

```sh
docker compose down -v
```

---

## 📂 Estructura del Proyecto

```
📂 MLOps-Taller1
│── 📂 jupyter_work/              # Directorio donde se guardan los notebooks
│── 📂 models/                    # Carpeta compartida para almacenar los modelos entrenados
│── 📜 docker-compose.yml          # Configuración de los servicios en Docker
│── 📜 README.md                   # Documentación del proyecto
```

---

## Acceso a JupyterLab

Una vez que el contenedor está en ejecución, puedes acceder a **JupyterLab** :

**URL de acceso:**
```
http://localhost:8888
```

El acceso está configurado para **no requerir token ni contraseña**.

