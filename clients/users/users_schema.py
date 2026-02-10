from pydantic import BaseModel, Field, ConfigDict, EmailStr

class UserSchema(BaseModel):
    """
    Описание модели пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    id : str
    email: EmailStr
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserRequestSchema(BaseModel):
    """
    Описание модели запроса на создание пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr
    password: str
    last_name: str = Field(alias="lastName")
    first_name: str = Field(alias="firstName")
    middle_name: str = Field(alias="middleName")

class CreateUserResponseSchema(BaseModel):
    """
    Описание модели ответа создания пользователя.
    """
    user: UserSchema

class UpdateUserRequestSchema(BaseModel):
    """
    Описание модели запроса на обновление пользователя.
    """
    model_config = ConfigDict(populate_by_name=True)

    email: EmailStr | None
    last_name: str | None = Field(alias="lastName")
    first_name: str | None = Field(alias="firstName")
    middle_name: str | None = Field(alias="middleName")

class GetUserResponseSchema(BaseModel):
    """
    Описание модели ответа запроса пользователя.
    """
    user: UserSchema