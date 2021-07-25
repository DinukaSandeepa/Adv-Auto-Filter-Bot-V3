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

USER_SESSION = os.environ.get("USER_SESSION")

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
