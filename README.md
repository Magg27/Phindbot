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
2. Install the required dependencies.
3. Replace the placeholder in `bot.run('')` with your Discord bot token.
4. Replace the placeholder in `/PATH/TO/CHROMIUM/` & `/PATH/TO/CHROMIUMDRIVER/` with your correct file locations.
5. Run the script.

## Usage

- `!search <question>`: The bot will perform a task based on the question and reply with the gathered information.
- `!clear`: The bot will clear the current thread removing all context from the conversation.

## Images

![Screenshot_20230724_200906](https://github.com/Magg27/Phindbot/assets/84076753/061459a0-9f70-4de0-84c1-7c54b1da4094)
![Screenshot_20230724_201018](https://github.com/Magg27/Phindbot/assets/84076753/1a72aa8c-ea71-42f6-89ae-37fa3794fde4)

## Note

This bot is intended for educational purposes only and should not be used for spamming or any form of abuse.


