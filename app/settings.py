import logging
import os
from typing import List

from dotenv import load_dotenv
from starlette.config import Config
from starlette.datastructures import CommaSeparatedStrings

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
config = Config(".env")
load_dotenv()


def get_env_tags(tag_list: List[str]) -> dict:
    """Create dictionary of available environment tags  """
    tags = {}
    for t in tag_list:
        tag_key, env_key = t.split(":")

        env_value = os.environ.get(env_key)

        if env_value:
            tags.update({tag_key: env_value})

    return tags


LOG_LEVEL = config("LOG_LEVEL", default=logging.DEBUG)
DEBUG = config("DEBUG", default=False, cast=bool)
ENV = config("ENV", default="local")
REGION_NAME = config("AWS_REGION", default=None)

AWS_PROFILE = config("AWS_PROFILE", default=None)
ENVIRONMENT_NAME = config("ENVIRONMENT_NAME", default=None, cast=str)
TITLE = "DYNAMIC-FORMS-REST-API" 
CONTACT_EMAIL = "support@tsworks.io"
URL = "https://tsworks.io"
VERSION = "1.0.0"
DESCRIPTION = "DYNAMIC FORMS"
STAGE = config("STAGE", default=None)
ENV_TAG_LIST = config("ENV_TAGS", cast=CommaSeparatedStrings, default="")
ENV_TAGS = get_env_tags(ENV_TAG_LIST)
ALLOWED_HOST = config("ALLOWED_HOST", default=["*"], cast=list)
CORS_ALLOWED_ORIGINS = config("ALLOWED_ORIGINS", default=["*"], cast=list)
CORS_ALLOWED_METHODS = ["POST", "GET", "PUT", "OPTIONS", "DELETE", "PATCH"]
CORS_ALLOWED_HEADERS = ["*"]
CONTACT = {
    "name": TITLE,
    "email": CONTACT_EMAIL,
}
OPENAPI_PREFIX = "/"
OPENAPI_URL = None if STAGE == "prod" else "/openapi.json"
REDOC_URL = None if STAGE == "prod" else "/docs"


SHOW_DOCS_ENVIRONMENT = ("local", "staging")
