import discord
import asyncio
import datetime

client = discord.Client()

distoken = NzE1OTc2ODE1MTAwOTUyNjA3.XtITeQ.1C79ng6gHis6aDM3BgtEgPenlFY

# These must all be Voice Channel
timechannel = # The ID of the Channel that gets renamed

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    while True:
        now = datetime.datetime.now()
        await client.get_channel(timechannel).edit(name=f"{now.hour}:{now.minute} (+8) # The channel gets changed here
        await asyncio.sleep(60)


client.run(distoken)
