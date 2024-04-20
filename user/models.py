from pydantic import BaseModel
import uuid

class User(BaseModel):
    '''User model'''
    
    id: uuid
    first_name: str
    last_name: str
    email: str
    phone_number: str
    