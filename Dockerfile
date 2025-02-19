# Usa una imagen base con Python
FROM python:3.11-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y curl python3-pip python3-venv

# Instalar `uv` usando el script oficial
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    mv /root/.local/bin/uv /usr/local/bin/

# Verificar que `uv` está instalado correctamente
RUN /usr/local/bin/uv --version

# Crear el directorio de trabajo
WORKDIR /app

# Copiar los archivos del proyecto
COPY . .

# Crear el entorno virtual e instalar dependencias con pip (no con uv)
RUN python3 -m venv /app/.venv && \
    /app/.venv/bin/python -m pip install --upgrade pip && \
    /app/.venv/bin/python -m pip install -r requirements.txt && \
    /app/.venv/bin/python -m pip install uvicorn  # Asegurar que uvicorn está instalado

# Verificar que uvicorn está correctamente instalado
RUN ls -la /app/.venv/bin && /app/.venv/bin/python -m uvicorn --version

# Exponer el puerto de FastAPI
EXPOSE 8000

# Comando de inicio (ejecutando uvicorn desde el entorno virtual)
CMD ["/app/.venv/bin/python", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
