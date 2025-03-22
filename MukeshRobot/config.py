class Config(object):
    LOGGER = True
    API_ID =None 
    API_HASH = ""
    TOKEN = ""  
    OWNER_ID=None
    
    SUPPORT_CHAT = "" 
    START_IMG = ""
    EVENT_LOGS = ()
    MONGO_DB_URI= ""
   
    DATABASE_URL = ""  # A sql database url from elephantsql.com
    CASH_API_KEY = (
        "3BQULWA5D2MRXNVS"
    )
    TIME_API_KEY = "CNLBLVHGMWPT"

    
    BL_CHATS = [] 
    DRAGONS = []
    DEV_USERS = []  
    DEMONS = [] 
    TIGERS = []  
    WOLVES = [] 

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True