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
4. Create a new Google Spreadsheet file and obtain the credentials JSON file. You can follow the instructions [here](https://mljar.com/blog/authenticate-python-google-sheets-service-account-json-credentials/).

## **Configuration**

1. Rename the `credentials-example.json` file to `config.json`.
2. Replace the placeholders in `config.json` with your own information.

## **Usage**

To start the bot, run `python main.py` in your terminal. The bot will be online and listening for YOUR created commands:
- Usually in the format `/bot-help` or `/bot-add input1 input2`

## **Credits**

This project was created by [czarolag](https://github.com/czarolag) with the help of [ChatGPT](https://chat.openai.com/). 
If you have any questions or suggestions, please feel free to contact me.
