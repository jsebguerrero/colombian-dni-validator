import uvicorn
from settings_handler import settings
from dotenv import load_dotenv
import os

load_dotenv()

PATH = os.path.dirname(os.path.realpath(__file__))

if __name__ == "__main__":
    uvicorn.run(
        "app:app",
        host = "0.0.0.0",
        port = 9001,
        reload = False,
        debug = False,
        log_level = "info",
        workers = 4
    )