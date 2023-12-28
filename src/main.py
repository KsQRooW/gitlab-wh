import logging

from fastapi import FastAPI

from . import config
from .app import GitLabWH
from .routers import main_router

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")

gitlab_wh = GitLabWH(
    app_type=FastAPI,
    main_router=main_router,
    static_folder_path=config.STATIC_FOLDER_PATH,
)
