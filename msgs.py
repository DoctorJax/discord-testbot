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
            await msg.channel.send("test")