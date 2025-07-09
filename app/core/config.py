from dotenv import load_dotenv
import os
from pydantic_settings import BaseSettings 

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../'))
DOTENV_PATH = os.path.join(BASE_DIR, '.env')

load_dotenv(dotenv_path=DOTENV_PATH)

class Settings(BaseSettings):
    DB_NAME: str = os.getenv("DB_NAME")
    DB_HOST: str = os.getenv("HOST")
    DB_USER: str = os.getenv("DB_USERNAME")
    DB_PASSWORD: str = os.getenv("PASSWORD")
    DB_PORT: str = os.getenv("DB_PORT")

    @property
    def database_url(self) -> str:
        return f"mysql+aiomysql://{self.DB_USER}:{self.DB_PASSWORD}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
    

settings = Settings()