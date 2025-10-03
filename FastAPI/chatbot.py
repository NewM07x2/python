import requests
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
OLLAMA_URL = "http://localhost:11434/v1/chat/completions"

class ChatRequest(BaseModel):
    model_alias: str = "gemma3:4b"
    question: str

@app.post("/chatbot")
async def chatbot(req: ChatRequest):
    payload = {
        "model": req.model_alias,
        "messages": [{"role": "user", "content": req.question}],
        "temperature": 0.2,
    }
    response = requests.post(OLLAMA_URL, json=payload).json()

    if response.get("choices") is None:
        return response["error"].get("message", "Error: No response from Ollama.")

    return response["choices"][0]["message"].get("content", "Error: No response from Ollama.")

"""
curl -X POST http://127.0.0.1:8000/chatbot \
     -H "Content-Type: application/json" \
     -d '{"model_alias":"gemma3:4b","question":"こんにちは、AIとは何ですか？"}'
""" 