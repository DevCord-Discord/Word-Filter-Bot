import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

    if message.content.startswith('$your mom'):
        await message.channel.send('Super gay')

client.run('ODA3MTkyNjU0MDQ2ODIyNDgw.YB0avQ.VHlt_rOv8Yrpuifoql9TUSMfOAU')