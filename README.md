# **DiscordBot**

This project is a Discord bot that allows you to update information on a Google Spreadsheet file using various commands. It can be easily modified to suit your own needs. The bot uses the following APIs:

- [hikari](https://github.com/hikari-py/hikari/)
- [hikari-lightbulb](https://github.com/tandemdude/hikari-lightbulb)
- [gspread](https://github.com/burnash/gspread)
- [discord.py](https://discord.com/developers/docs/intro)

## **Installation**

1. Clone the repository: `git clone https://github.com/your-username/DiscordBot.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Set up a new Discord bot and obtain the bot token. You can follow the instructions [here](https://discord.com/developers/docs/getting-started).
4. Create a Service Account and obtain the credentials JSON file. You can follow the instructions [here](https://mljar.com/blog/authenticate-python-google-sheets-service-account-json-credentials/).
5. Create a Google Sheets and get the [Google Sheets ID](https://developers.google.com/sheets/api/guides/concepts).

## **Configuration**

1. Create a copy and rename `credentials-example.json` to `credentials.json` by running `cp credentials-example.json credentials.json`.
2. Replace the placeholders in `credentials.json` with your own information `NOTE: Only modify the newly created credentials.json`
3. Create a copy and rename `bot_data_example.json` to `bot_data.json` by running `cp bot_data_example.json bot_data.json`.
4. Update information in `bot_data.json` with your own information `NOTE: Only modify the newly created bot_data.json`

## **Usage**

To start the bot, run `python discordbot.py` in your terminal. The bot will be online and listening for YOUR created commands:
- Usually in the format `/bot-help` or `/bot-add input1 input2`

## **Credits**

This project was created by [czarolag](https://github.com/czarolag) with the help of [ChatGPT](https://chat.openai.com/). 
If you have any questions or suggestions, please feel free to contact me.
