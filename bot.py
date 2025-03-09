# TTRPG Server Bot
# Created for DM Rebecca's TTRPG Server on Discord 
# Authored by @ymir5578 | Prince_of_Galar

#-------------------- SETUP --------------------#

import discord
import asyncio
import os
import re
from discord.utils import get
from discord.ext import commands

#--------------- GLOBAL VARIABLES ---------------#

client = discord.Client(intents=discord.Intents.default())

#-------------------- GREET + ROLE(?) USERS ON JOIN --------------------#

@client.event
async def on_member_join(member):
    channel = client.get_channel(id = 681917060556783718)
    role = member.guild.get_role(role_id = rolesIndex[28])
    await channel.send('A new adventurer has entered the dungeon! Please welcome {}'.format(member.mention) + '!')
    #await member.add_roles(role)

#-------------------- CHECK & RESPOND TO MESSAGES --------------------#  

@client.event 
async def on_message(message):
    if message.channel.type != discord.ChannelType.private and message.author != client.user: # make sure message author is not the bot itself
        
        #Tour-help command
        if splitMessage[0] == '!helpFGU':
            FGUCommandsGuide = discord.Embed()
            FGUCommandsGudie.title = '***FGU Commands Help***'
            FGUCommandsGuide.add_field(name = 'Connection Info', value = '_User Name_: zeldaharvestmoon\n_Campaign Name_: LMP0001\n_Password_: LMP0001')
            FGUCommandsGuide.add_field(name = 'Close Error Console', value = '`/console skip`')
            FGUCommandsGuide.add_field(name = 'Whisper', value = '`w/ CharacterName ChatMessage`\nTo whisper to the DM, use `w/ GM ChatMessage`')
        await message.channel.send(embed = FGUCommandsGuide)

#-------------------- RUN TTRPG SERVER BOT --------------------#

@client.event
async def on_ready():
    print('TTRPG Server Bot is ready to assist!')

#Runs the app
if __name__ == '__main__':
    client.run(os.environ.get('TOKEN'))