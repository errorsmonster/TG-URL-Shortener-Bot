import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.environ.get("API_ID", "26180065")) #API ID from https://my.telegram.org/auth
API_HASH = os.environ.get("API_HASH", "0a6358307acf8d0d2bf98b6827e0f5c7") #API Hash from https://my.telegram.org/auth
BOT_TOKEN = os.environ.get("BOT_TOKEN", "6992264465:AAFLUE_QV50Ly9OBpp3IGAo_mkMyfl984-4") # Bot token from @BotFather
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS", "6072149828").split(",")] if os.environ.get("ADMINS") else [] #Keep thia empty otherwise bot will not work for owner.
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "shortener")
DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://errorsmonster:S.Aruna1155182089@shortener.woficdt.mongodb.net/?retryWrites=true&w=majority") # mongodb uri from https://www.mongodb.com/
OWNER_ID =  int(os.environ.get("OWNER_ID", "6072149828")) # id of the owner
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(6390495622)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002115739348")) # log channel for information about users
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "MrAK_LinkZz") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "False") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", 'https://graph.org/file/8cd764fbdf3ccd34abe22.jpg') # image when someone hit /start
LINK_BYPASS = "True" 
"""
   _____                    __  __         _    _              _       _______           _     
  / ____|                  |  \/  |       | |  | |            ( )     |__   __|         | |    
 | |  __  _ __  ___  _   _ | \  / |  __ _ | |_ | |_  ___  _ __|/ ___     | |  ___   ___ | |__  
 | | |_ || '__|/ _ \| | | || |\/| | / _` || __|| __|/ _ \| '__| / __|    | | / _ \ / __|| '_ \ 
 | |__| || |  |  __/| |_| || |  | || (_| || |_ | |_|  __/| |    \__ \    | ||  __/| (__ | | | |
  \_____||_|   \___| \__, ||_|  |_| \__,_| \__| \__|\___||_|    |___/    |_| \___| \___||_| |_|
                      __/ |                                                                    
                     |___/                                                                     
Author: GreyMatter's Tech
GitHub: https://GreyMattersTech.com/GitHub
Website: https://GreyMattersTech.com
"""
