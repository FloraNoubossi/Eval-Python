# Eval-Python
# FastAPI Application pour Intégration avec l'API Groq

## Description

J'ai développé cette application avec **FastAPI** pour interagir avec l'API **Groq**. L'application est capable de traiter des requêtes de chat en utilisant le modèle `mixtral-8x7b-32768` via des endpoints HTTP.

### Fonctionnalités principales :

- **/status** : Un endpoint GET pour vérifier l'état de l'API.
- **/chat** : Un endpoint POST qui prend un prompt et retourne une réponse générée par l'API Groq.

## Prérequis

Avant de lancer l'application, j'ai configuré quelques éléments nécessaires pour garantir son bon fonctionnement.

### Ce dont j'ai besoin :

- **Python 3.8 ou plus récent**
- **FastAPI** pour gérer les requêtes HTTP.
- **Uvicorn** pour exécuter le serveur ASGI.
- **groq** (le SDK pour interagir avec l'API Groq)
- **pydantic** pour valider les données.

J'ai installé ces dépendances à partir du fichier `requirements.txt` :

```bash
pip install -r requirements.txt


Configuration de l'environnement
Pour faire fonctionner l'application, j'ai besoin d'une clé API valide de l'API Groq. Cette clé est stockée dans les variables d'environnement
GROQ_API_KEY=ma_cle_api_groq

Endpoints
GET /status
Cet endpoint permet de vérifier si l'API est en ligne.

Exemple de réponse :
{
  "message": "OK"
}

POST /chat
Cet endpoint prend un prompt de type texte, envoie la requête à l'API Groq, et renvoie la réponse du modèle.

Exemple de corps de la requête :

{
  "prompt": "What is a LLM?"
}

{
  "response": "A large language model (LLM) is a machine learning model..."
}





