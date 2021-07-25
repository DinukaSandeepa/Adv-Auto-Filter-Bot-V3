#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = int(os.environ.get("1627545"))

API_HASH = os.environ.get("64e277a5e717aec5fecd067a34c35460")

BOT_TOKEN = os.environ.get("1920925746:AAHISIGnxxSsNWtciZ-2OktBYadNwKGrf7U")

DB_URI = os.environ.get("mongodb+srv://dinukacreation:dinukacreation@cluster0.cidiq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")

USER_SESSION = os.environ.get("BQAaKQH3WyUBipinuArvmfWPcYMBNzelC83cH30B9crPbX6A3NCwKyi6zXsk-rEMYmxN180a2V417djjsrFfNaCjNxMq9M0ZrzabrgncoMquJH9JuCH5t6FrnqW5-gcfw4Y6MZRkglYCb2lQG4Nn1yVmQ6Qq6mmGP68D2o6wT5TsuPyfAkeA9KGp9fizknOIOVWaZgiCiBhIGJ-qZN4Lc-5RyVnvudqFPK7bilhsPMAZFt7xDMyWz2MBZpVehUOYlNooXT0ohtRn18aXWpytwr2Y_qVMg49Iui3GaxLYsBBOysi1fx_lU5AOgkMup-mrq6jTjhwLV9hjumn66Q8VqKxLL7Wt5QA")

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
