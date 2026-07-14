#(©)CodeXBotz

import os
import logging
from dotenv import load_dotenv
from logging.handlers import RotatingFileHandler

load_dotenv()

#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "8237959420:AAHE0atddUSOCosRnwWxqPNSB6E8We2xjz4")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("API_ID", 37063855))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0419e8626a4ac694ff59f0953c7d089e")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID"," -1003915205339", " -1003776613512"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "@Yabibal_90"))

#Port
PORT = os.environ.get("PORT", "8080")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://dokimasfkir_db_user:7jd5JqiT8bR9EqiL@cluster0.z21m00y.mongodb.net/?appName=Cluster0")
DB_NAME = os.environ.get("DATABASE_NAME", "filesharexbot")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL"," -1003915205339", " -1003776613512"))
JOIN_REQUEST_ENABLE = os.environ.get("JOIN_REQUEST_ENABLE", "True").lower() == "true"

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "8"))

#start message
START_PIC = os.environ.get("START_PIC","https://t.me/hind_amharic_et/119.jpg")
START_MSG = os.environ.get("START_MESSAGE", "
ሰላም **{first}**! 😊

ይህ ቦት ፊልሞችን ለማግኘት እና ለማውረድ ይረዳዎታል። 

እባክዎ ከመጠቀምዎ በፊት የእኛን ቻናሎች ይቀላቀሉ።

[የህንድ ተከታታይ ፊልሞች🍿](https://t.me/hind_amharic_et)
[Chandra Nandini በትርጉም🇪🇹](https://t.me/Hind_Amharic_ETH)
")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Hello {first}\n\n<b>You need to join in my Channel/Group to use me\n\nKindly Please join Channel</b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

# Auto delete time in seconds.
AUTO_DELETE_TIME = int(os.getenv("AUTO_DELETE_TIME", "0"))
AUTO_DELETE_MSG = os.environ.get("AUTO_DELETE_MSG", "This file will be automatically deleted in {time} seconds. Please ensure you have saved any necessary content before this time.")
AUTO_DEL_SUCCESS_MSG = os.environ.get("AUTO_DEL_SUCCESS_MSG", "Your file has been successfully deleted. Thank you for using our service. ✅")

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "❌Don't send me messages directly I'm only File Share bot!"

ADMINS.append(OWNER_ID)
ADMINS.append(8137681106)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
