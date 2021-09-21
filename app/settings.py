"""
Module to import or set module-level variables.
"""
import os

from dotenv import load_dotenv

load_dotenv()

BOT_PREFIX = os.getenv("BOT_PREFIX")
TOKEN = os.getenv("TOKEN")
OWNERS = os.getenv("OWNERS")
APPLICATION_ID = os.getenv("APPLICATION_ID")
