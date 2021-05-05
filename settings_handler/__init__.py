from dotenv import load_dotenv
from dotenv_settings_handler import BaseSettingsHandler

__all__ = ("settings",)

load_dotenv()


class Settings(BaseSettingsHandler):


    class Config:
        case_insensitive = True


settings = Settings()
