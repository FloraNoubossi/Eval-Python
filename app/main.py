from dotenv import load_dotenv

# Charger les variables depuis le fichier .env
load_dotenv()


import os
import groq
from groq import Groq
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Configure the API key
api_key = os.environ.get("GROQ_API_KEY")
if not api_key:
    raise ValueError("API key not set in environment variables")

client = Groq(
    api_key=api_key,
    timeout=20.0,
    max_retries=1,
)

class Prompt(BaseModel):
    prompt: str

@app.get("/status")
async def get_status():
    return {"message": "OK"}

@app.post("/chat")
async def post_chat(prompt: Prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant.",
                },
                {
                    "role": "user",
                    "content": prompt.prompt,
                },
            ],
            model="mixtral-8x7b-32768",
        )
        return {"response": chat_completion.choices[0].message.content}

    except groq.APIConnectionError as e:
        print("The server could not be reached")
        raise HTTPException(status_code=500, detail="API Connection Error")

    except groq.RateLimitError as e:
        print("A 429 status code was received; we should back off a bit.")
        raise HTTPException(status_code=429, detail="Rate Limit Exceeded")

    except groq.APIStatusError as e:
        print(f"Non-200 status code received: {e.status_code}")
        raise HTTPException(status_code=e.status_code, detail="API Status Error")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
