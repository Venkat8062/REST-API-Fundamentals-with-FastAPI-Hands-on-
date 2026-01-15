from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Calculator API")


# -------- Data Model --------
class CalculationRequest(BaseModel):
    a: float
    b: float
    operation: str


# -------- Health Endpoints --------
@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/ready")
def readiness():
    return {"status": "ready"}


# -------- Calculator Endpoint --------
@app.post("/calculate")
def calculate(data: CalculationRequest):
    if data.operation == "add":
        result = data.a + data.b
    elif data.operation == "subtract":
        result = data.a - data.b
    elif data.operation == "multiply":
        result = data.a * data.b
    elif data.operation == "divide":
        if data.b == 0:
            raise HTTPException(status_code=400, detail="Division by zero is not allowed")
        result = data.a / data.b
    else:
        raise HTTPException(
            status_code=400,
            detail="Invalid operation. Use add, subtract, multiply, or divide."
        )

    return {
        "a": data.a,
        "b": data.b,
        "operation": data.operation,
        "result": result
    }
