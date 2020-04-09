#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import os
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, RegexHandler
from dotenv import load_dotenv

from lib.retrievers import random_bike_photo, filter_retrieve_string, bike_specs, chicho_response

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
load_dotenv()

BOT_KEY = os.getenv("DUCATI_BOT_KEY")

updater = Updater(BOT_KEY, use_context=True)

KEY_WORDS =["bot", "como dios manda"]


def handle_message(update, context):
    bot = context.bot
    message_text = str(update.message.text).lower()
    chat_id = update.message.chat.id

    if not any(occurrence in message_text for occurrence in KEY_WORDS):
        return

    text_to_reply = None

    image_matchers = ["foto", "photo", "image"]
    specs_matchers = ["ficha", "specs", "motofichas", "informacion", "información"]
    thanks_message = "Gracias {}, se agradece!"
    sorry_message = "Hago lo que puedo 😞. Intentaré hacerlo mejor la próxima vez, {}"

    if any(occurrence in message_text for occurrence in image_matchers):
        max_index = 0
        max_matcher = None
        for matcher in image_matchers:
            try:
                found_index = message_text.index(matcher)
                if found_index > max_index:
                    max_index = found_index
                    max_matcher = matcher
            except:
                pass
        search_message = message_text.split(max_matcher)[1] if max_matcher else message_text
        print("SEARCHING BIKE PHOTO FOR TEXT: {}".format(filter_retrieve_string(search_message)))
        text_to_reply = random_bike_photo(filter_retrieve_string(search_message))
    elif any(occurrence in message_text for occurrence in specs_matchers):
        max_index = 0
        max_matcher = None
        for matcher in specs_matchers:
            try:
                found_index = message_text.index(matcher)
                if found_index > max_index:
                    max_index = found_index
                    max_matcher = matcher
            except:
                pass
        search_message = message_text.split(max_matcher)[1] if max_matcher else message_text
        print("SEARCHING SPECS PAGE FOR TEXT: {}".format(filter_retrieve_string(search_message)))
        text_to_reply = bike_specs(filter_retrieve_string(search_message))
    elif "como dios manda" in message_text:
        text_to_reply = chicho_response()
    elif "mierda" in message_text or "cagao" in message_text or "basura" in message_text:
        bot.send_message(chat_id, sorry_message.format(update.message.from_user.first_name))
        return
    elif "buen" in message_text:
        bot.send_message(chat_id, thanks_message.format(update.message.from_user.first_name))
        return

    if text_to_reply:
        if text_to_reply == -1:
            bot.send_message(chat_id, "No he encontrado nada :(")
        else:
            bot.send_message(chat_id, text_to_reply)


updater.dispatcher.add_handler(RegexHandler(".*", handle_message))

updater.start_polling()
updater.idle()
