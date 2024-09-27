# Dockerfile
FROM python:3.9-slim

# Définit le répertoire de travail
WORKDIR /app

# Copie le fichier requirements.txt
COPY requirements.txt .

# Installe les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copie tout le reste du code source
COPY . .

# Expose le port que l'application FastAPI utilisera
EXPOSE 5000

# Commande pour démarrer l'application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]

