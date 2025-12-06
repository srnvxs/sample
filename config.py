import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5893707486:AAFjecY2CC6oyMKXD6c3XDbm9UKUdPuacfE")
    APP_ID = int(os.environ.get("APP_ID", 12210813))
    API_HASH = os.environ.get("API_HASH", "e42eeae11a2f96bcfc5ec3b46a30adad")
