from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    workerai_api_key:str
    workerai_account_id:str

    class Config:
        env_file=".env"



SETTINGS  = Settings()