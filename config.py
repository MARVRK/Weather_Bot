from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    TELEGRAM_TOKEN : str
    CHANNEL_ID : int
    CITY : str
    COUNTRY_CODE : str
    MEASUREMENT : str
    API_KEY_WEATHER : str
    MYSQL_DATABASE: str
    MYSQL_USER: str
    MYSQL_PASSWORD: str
    MYSQL_HOST: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

config = Settings()
