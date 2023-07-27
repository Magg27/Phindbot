# Phind Bot

This repository contains a Discord bot that uses Selenium WebDriver for web scraping. The bot responds to user commands and replies to the user with the gathered information.

## Features

- The bot connects to Discord and listens for user messages.
- It responds to two commands: `!search` and `!clear` (possibly more to come in future).
- The `!search` command takes a question as input, performs a web scraping task, and replies with the scraped information.
- The `!clear` command clears the current thread.

## Dependencies

- Selenium WebDriver
- Undetected Chromedriver
- Discord.py
- Colorama

## Setup

1. Clone this repository.
2. Install the required dependencies
3. Put your discord token and the path to your chromium installation in the `.env` file 
4. Run the script.

## Usage

- `!search <question>`: The bot will perform a task based on the question and reply with the gathered information.
- `!clear`: The bot will clear the current thread removing all context from the conversation.

## Note

This bot is intended for educational purposes only and should not be used for spamming or any form of abuse.


