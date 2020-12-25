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
                description="I'm currently in development, but here are a few commands you can do: \n !help (I don't have to tell you what this does) \n !roll <number>*[multiplier]",
                color=discord.Color.from_rgb(0,0,255)
            ))