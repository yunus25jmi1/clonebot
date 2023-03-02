import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    TG_BOT_TOKEN = "6263835773:AAHR_BB-kuAWUIlaGdr-4nOtKV5SCMjltUY"
    APP_ID = 7946647
    API_HASH = "3d564ea96a493b54f8aa5ebb3408bb9f"
    TG_USER_SESSION = "BQB5QZcAFLhT8lwzlK63TdMw6elQQuiRZNrNTs2qKmiVXzWQwMetrGcfHXrXP_Ud7s62Iq0AWqwAgqrFDsMnyRE0sM0n2FzW1SVAj0_35tJGdPf_pExzBGAokcblL4-_yWc7xnBd81MpXYbRTx5r1XdzUYjl6pWPyOg-KMKHdrOmWK1TZIWmp4Knr0LaainaPZMtrlpKIXMw3iaqIuqeoSQfbKxBbZR7aK0ZqC7gslBt672PnzsPBC1j9PPVwfgrJW78SiiuJA26dkO_kjvqE7QM-dZmXWVWkepAUPYG8cEpgHBx25grf9bdsXFTuFSRG9bYM43donTZfaEFuupacuMJicnntgAAAABr_tVzAA"
    DB_URI = ""

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
