#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
import requests
from random import randint
from telegram.ext import Updater, CommandHandler
from dotenv import load_dotenv

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
load_dotenv()

GOOGLE_IMG_SEARCH_KEY = os.getenv("GOOGLE_IMG_SEARCH_KEY")
GOOGLE_CX = os.getenv("GOOGLE_CX")
QUERY = "Ducati Panigale"

updater = Updater(os.getenv("DUCATI_BOT_KEY"), use_context=True)


def get_image(update, context):
    request_url = "https://www.googleapis.com/customsearch/v1?cx={cx}&key={key}&searchType=image&q={query_text}".format(cx=GOOGLE_CX, key=GOOGLE_IMG_SEARCH_KEY, query_text=QUERY)
    result = requests.get(request_url)
    each_result = result.json()["items"]
    image_url = each_result[randint(0, len(each_result))]["link"]
    update.message.reply_text(image_url)


updater.dispatcher.add_handler(CommandHandler('get', get_image))

updater.start_polling()
updater.idle()
