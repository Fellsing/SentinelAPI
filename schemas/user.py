from pydantic import BaseModel, EmailStr, Field, ConfigDict


class UserBase(BaseModel):
    email: EmailStr = Field(max_length=100, min_length=8)

class UserCreate(UserBase):
    hashed_password: str = Field(max_length=200, min_length=8)

class UserRead(UserBase):
    id:int
    is_active:bool = False

    model_config = ConfigDict(from_attributes=True)