import os

class Config(object):
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "7900540474:AAGAjIQTUusUvx5Zk21TlqYmMJVyWRTnSEo")
    APP_ID = int(os.environ.get("APP_ID", 12210813))
    API_HASH = os.environ.get("API_HASH", "e42eeae11a2f96bcfc5ec3b46a30adad")
