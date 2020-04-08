#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import requests
from random import randint
from dotenv import load_dotenv

load_dotenv()

GOOGLE_SEARCH_KEY = os.getenv("GOOGLE_SEARCH_KEY")
GOOGLE_CX = os.getenv("GOOGLE_CX")

ES_SYMBOLS = ["?", "!", ",", ".", ";", ":", "'", "\""]


def filter_retrieve_string(raw_string: str) -> str:
    """ Returns a filtered strings without spanish prepositions or some symbols. """
    final_string = raw_string
    for sym in ES_SYMBOLS:
        final_string = final_string.replace(sym, " ")
    return final_string


def random_bike_photo(search_query: str) -> str:
    """ Returns a random motorcycle photo URL matching the search_query contents. """
    search_query = "{}".format(search_query)
    request_url = "https://www.googleapis.com/customsearch/v1?cx={cx}&key={key}&searchType=image&q={query_text}".format(cx=GOOGLE_CX, key=GOOGLE_SEARCH_KEY, query_text=search_query)
    result = requests.get(request_url).json()

    if "error" in result.keys() and "daily limit" in result["error"]["message"]: 
        return "Nada chavales, se acabó el límite diario de búsquedas. A spamear a otro lado."

    if "items" not in result.keys():
        return -1

    each_result = result["items"]
    image_url = each_result[randint(0, len(each_result) - 1)]["link"]
    return image_url


def bike_specs(search_query: str) -> str:
    """ Returns a given motorcycle specs url. """
    search_query = "motorcycle specs {}".format(search_query)
    request_url = "https://www.googleapis.com/customsearch/v1?cx={cx}&key={key}&q={query_text}".format(cx=GOOGLE_CX, key=GOOGLE_SEARCH_KEY, query_text=search_query)
    result = requests.get(request_url).json()

    if "error" in result.keys() and "daily limit" in result["error"]["message"]: 
        return "No puedo buscar más fichas hasta mañana. Sorry 😅."

    if "items" not in result.keys():
        return -1

    each_result = result["items"]
    specs_url = each_result[0]["link"]
    return specs_url
