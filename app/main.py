from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, AIMessage

from utils import extract_csv_info
from chains import create_vector_store, create_recurring_chain
import config  # This ensures .env and key check runs

# Define the FastAPI app
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://cdd-app.vercel.app"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request schema
class ChatRequest(BaseModel):
    question: str

# Global state
csv_file_path = "annotated_data.csv"
documents = extract_csv_info(csv_file_path)
vectorStore = create_vector_store(documents)
chain = create_recurring_chain(vectorStore)
chat_history = []

@app.post("/ask")
async def chat(request: ChatRequest):
    global chat_history
    question = request.question

    try:
        response = chain.invoke({
            "chat_history": chat_history,
            "input": question,
        })
        answer = response["answer"]

        # Update history
        chat_history.append(HumanMessage(content=question))
        chat_history.append(AIMessage(content=answer))

        return {"response": answer}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the app
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
