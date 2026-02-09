from pydantic import EmailStr, BaseModel, Field


class UserSchema(BaseModel):
    """Модель данных пользователя"""
    id: str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")


class CreateUserRequestSchema(BaseModel):
    """Модель данных запроса создания пользователя"""
    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """Модель данных ответа создания пользователя"""
    user: UserSchema
