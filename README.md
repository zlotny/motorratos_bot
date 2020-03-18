# Ducati Bot

This bot aims to display an image for a Ducati product / search whenever the user wants.

It uses Google Custom search API and requires it to be setup to work correctly.

# Setup

## Installation
To run the bot you'll need to install the dependencies:

In GNU/Linux systems you'll need to run this as root.

```
pip install -r requirements.txt
```

## Configuration

You'll need to create an `.env` file on the root of the project with a content like this:

```
DUCATI_BOT_KEY=[YOUR_API_KEY]
GOOGLE_IMG_SEARCH_KEY=[YOUR_API_KEY]
GOOGLE_CX=[YOUR_CX_ID]
```

`DUCATI_BOT_KEY` would be the Telegram bot API key for the bot
`GOOGLE_IMG_SEARCH_KEY` is the key for the Google Search API
`GOOGLE_CX` is the identifier for the custom search engine