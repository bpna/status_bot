# Author: Patrick Kinsella
# Date last modified: 10/28/2012

import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
statuses = {}

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if client.user in message.mentions:
        nick = str(message.author).split('#')[0]
        raw_msg = message.clean_content
        status = raw_msg.split('@status_bot')[-1]
        statuses[nick] = status
    
    for role in message.role_mentions:
        if str(role) == 'dota':
            current_statuses = '\n'.join('{} is {}'.format(k, v) for k, v in statuses.items())
            await message.channel.send(current_statuses)
    
    print(f'channel is: {message.channel}')
    print(f'message content is: {message.content}')
    print(f'role mentions are: {message.role_mentions}')
    print(f'mentions are: {message.mentions}')
  
client.run(TOKEN)
