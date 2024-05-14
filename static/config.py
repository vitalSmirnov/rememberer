import json
import os
API_ID = 0
API_HASH = ""
BOT_TOKEN = ""
GROUP_ID = ""

if os.path.exists("config.json"):
    with open("config.json", "r", encoding="utf-8") as json_conf:
        credentials = json.load(json_conf)

        API_ID = credentials.get("api_id")
        API_HASH = credentials.get("api_hash")
        BOT_TOKEN = credentials.get("bot_token")
        GROUP_ID = credentials.get("main_group_id")
