import lightbulb
from hikari import Embed
import gspread
import json

import google.auth
from google.auth.transport.requests import Request

'''
Method returns needed data for the bot to function, using key, value pairs from 'bot_data.json'
'''
def getData(key: str):
    with open('bot_data.json', 'r') as f:
        data = json.load(f)

    value = data[key]
    return value


# Authenticate the bot by creating it and adding the token
# More on this: https://discord.com/developers/docs/intro
bot = lightbulb.BotApp(
    token=getData("token"),
    default_enabled_guilds=(
        getData("guild_1")
        )
)

# credentials.json for service account must be in same directory. Steps can be found: https://mljar.com/blog/authenticate-python-google-sheets-service-account-json-credentials/
creds, project_id = google.auth.load_credentials_from_file('credentials.json', scopes=['https://www.googleapis.com/auth/spreadsheets'])

if not creds or not creds.valid:
    creds.refresh(google.auth.transport.requests.Request())


'''
Example Command used to display commands created.
'''
@bot.command
@lightbulb.command('bot-help', 'Provides commands') # command to be used from discord ex: /bot-help ~ provides commands
@lightbulb.implements(lightbulb.SlashCommand) # '/' must be used to use the command: /bot-help
async def help(ctx):
    # example list to display various commands. Can append more commands if needed
    info = [
            '/bot-display {column}',
            '/bot-temp {example for own use}'
            ]

    # creates an embed in discord. More about embeds: https://b1naryth1ef.github.io/disco/bot_tutorial/message_embeds.html
    embed = Embed(
            title=f"Bot Commands",
            description='\n'.join(info),
            color=0x2b76c3,
        )

    # used to create a respose by the bot in discord. This will display the embed created to the server
    await ctx.respond(embed=embed)


'''
Example Command displays a column from the Google Sheets to the discord server
'''
@bot.command
@lightbulb.option('column', 'Column to display', type=int)
@lightbulb.command('bot-display', 'Displays a column on the google sheets')
@lightbulb.implements(lightbulb.SlashCommand)
async def display(ctx):
    # Uses credentials.json to recieve service account
    gc = gspread.service_account(filename='credentials.json')    

    # Used to modify information of Google Sheets using ID recieved from 'bot_data.json'
    # More about gspread API commands: https://github.com/burnash/gspread/tree/v5.7.1
    sheet_id = getData("sheet_id_1")
    wks = gc.open_by_key(sheet_id)
    sh = wks.get_worksheet(0)

    # get info in a column
    values_list = sh.col_values(ctx.options.column)

    embed = Embed(
            title=f"Info From Column {ctx.options.column}",
            description='\n'.join(values_list),
            color=0x2b76c3,
        )

    # respond the information onto the server
    await ctx.respond(embed=embed)

# runs the bot
bot.run()