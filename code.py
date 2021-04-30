import discord

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('hello'):
        await message.channel.send('hello, I am a bot')

client.run('ODM3MDExNTQ4MzI4NTU4NjQy.YImVwA.uyVQ37eLymHL2Kt2v76eCbR8GR4')