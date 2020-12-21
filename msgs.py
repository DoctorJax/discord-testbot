#!/usr/bin/python
import os, discord
import func

### Run when a command message is sent (that the bot can read)
async def on_message(msg):
    # Only works in a channel named "idk"
    if str(msg.channel) == 'idk':
        # Works if command is "!roll"
        if str(msg.content)[:6] == '!roll ':
            # Call roll command in func.py
            await func.roll(msg, str(msg.content)[6:])
        if str(msg.content)[:6] == '!help':
            await msg.channel.send(embed=discord.Embed(
                title="!Help",
                description="1 \n 2 \n 3",
                color=discord.Color.from_rgb(0,0,255)
            ))