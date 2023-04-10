import lightbulb
from hikari import Embed
import gspread

import google.auth
from google.auth.transport.requests import Request

# Authenticate the bot by creating it and adding the token
# More on this: https://discord.com/developers/docs/intro
bot = lightbulb.BotApp(
    token='Your Bot Token Here',
    default_enabled_guilds=(
        0000000000000000, # Your discord Server ID here. Can be more than one server (Servers are also known as Guilds)
        1111111111111111,
        )
)

SPREADSHEET_ID = 'Google Spreadsheet ID here'
creds = None

# credentials.json for service account must be in same directory. Steps can be found: https://mljar.com/blog/authenticate-python-google-sheets-service-account-json-credentials/
creds, project_id = google.auth.load_credentials_from_file('Your_Service_Account_Credentials.json', scopes=['https://www.googleapis.com/auth/spreadsheets'])

if not creds or not creds.valid:
    creds.refresh(google.auth.transport.requests.Request())


'''
Command Options can be used within discord chat
'''
@bot.command
@lightbulb.command('bot-help', 'Provides commands') # command to be used from discord ex: /bot-help ~ provides commands
@lightbulb.implements(lightbulb.SlashCommand) # '/' must be used to use the command: /bot-help
async def help(ctx):
    # example list to display various commands. Can append more commands if needed
    info = [
            '/bot-add {information}',
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
Command Option with user input
'''
@bot.command
@lightbulb.option('info_one', 'Input information 1', type=int)
@lightbulb.option('info_two', 'Input information 2', type=str)
@lightbulb.command("bot-addInfo", 'adds information to Google Spreadsheet')
@lightbulb.implements(lightbulb.SlashCommand) # Command: /bot-addInfo info_one info_two
async def equipment_max(ctx):

    # activates service account with given credentials.json
    gc = gspread.service_account(filename='Your_Service_Account_Credentials.json')

    # More about gsspread API commands: https://github.com/burnash/gspread/tree/v5.7.1
    sheet = gc.open_by_key(SPREADSHEET_ID)
    worksheet = sheet.worksheet('example_sheet')
    worksheet.update('A1', ctx.options.info_one) #ctx.options.example recieves the inputted information from the decorator @lightbulb.option('example', 'example info') 
    worksheet.update('B1', ctx.options.info_two)

    # using ctx.author.id in this format returns the username of the user who
    # has send the command request
    await ctx.respond(f'<@{ctx.author.id}> your info has been updated')


# runs the bot
bot.run()