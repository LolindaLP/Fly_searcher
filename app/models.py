from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    password: str

class Transaction(BaseModel):
    user_id: str
    amount: float
    category: str
    date: str
    description: str

class Budget(BaseModel):
    user_id: str
    amount: float
    category: str
    start_date: str
    end_date: str
