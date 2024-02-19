from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "21948646"))
    API_HASH = getenv("API_HASH", "289bdc44e67dc6992150dd8cf731c5b7")
    BOT_TOKEN = getenv("BOT_TOKEN", "6891263386:AAGdH44TNWeShyBn0qma1DEcpXBAAGksl9A")
    FSUB = getenv("FSUB", "")
    CHID = int(getenv("CHID", ""))
    SUDO = list(map(int, getenv("SUDO", "5521380948").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://Rohit44:Rohit44@cluster0.pfgkii2.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()
