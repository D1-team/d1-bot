"""
Module to import or set module-level variables.
"""
import os

from environ import Env

# Initialise environment variables
env = Env()
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

env.read_env(env_file=os.path.join(BASE_DIR, ".env"))

BOT_PREFIX = env("BOT_PREFIX", cast=str)
TOKEN = env("TOKEN", cast=str)
APPLICATION_ID = env("APPLICATION_ID", cast=str)
CPUS_PER_TASK = env("CPUS_PER_TASK", cast=int)
DATABASE_HOST = env("DATABASE_HOST", cast=str)
DATABASE_NAME = env("DATABASE_NAME", cast=str)
DATABASE_PASS = env("DATABASE_PASS", cast=str)
DATABASE_PORT = env("DATABASE_PORT", cast=str)
DATABASE_USER = env("DATABASE_USER", cast=str)
SECRET_KEY = env("SECRET_KEY", cast=str)
DEBUG = env("DEBUG", cast=bool)
USE_S3 = env("USE_S3", cast=bool)
AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME", cast=str)
AWS_S3_CUSTOM_DOMAIN = env("AWS_S3_CUSTOM_DOMAIN", cast=str)
SERVER_URL = env("SERVER_URL", cast=str)
