import sys
import uvicorn
from pathlib import Path
from fastapi import FastAPI

# add current path to sys path
sys.path.append(str(Path(__file__)))
from src.config import Config
from src.routes import init_routes
from src.middlewares import init_middlewares
from dotenv import dotenv_values

Config.load_env(dotenv_values())
app = FastAPI(debug=Config.is_debug_mode(), port=Config.get_app_port())
init_middlewares(app)
init_routes(app)


def main():
    uvicorn.run(app, host="0.0.0.0", port=Config.get_app_port())


if __name__ == "__main__":
    main()
