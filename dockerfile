# Imagen base
FROM python:3.11-slim

# Directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar dependencias e instalar
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de archivos
COPY . .

# Exponer el puerto en el que corre Flask
EXPOSE 5000

# Comando para ejecutar la app
CMD ["python", "main.py"]
