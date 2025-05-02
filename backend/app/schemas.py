from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    student_id: str
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class EventCreate(BaseModel):
    title: str
    description: str
    location: str
    date: datetime
    time: datetime

class EventRegistration(BaseModel):
    event_id: int
    qr_code: str