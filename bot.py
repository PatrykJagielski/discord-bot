import discord
import requests
import json
import asyncio

client = discord.Client()


def get_question():
    qs = ""
    id = 1
    answear = 0
    response = requests.get("http://sheltered-mesa-78550.herokuapp.com/api/random/")
    json_data = json.loads(response.text)
    qs += "Question: \n"
    qs += json_data[0]["title"] + "\n"

    for item in json_data[0]["answear"]:
        qs += str(id) + ". " + item["answear"] + "\n"

        if item["is_correct"]:
            answear = id

        id += 1

    return (qs, answear)


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$q"):
        qs, answear = get_question()
        await message.channel.send(qs)

        def check(m):
            return m.author == message.author and m.content.isdigit()

        try:
            guess = await client.wait_for("message", check=check, timeout=5.0)
        except asyncio.TimeoutError:
            return await message.channel.send("Sorry, you took too long")

        if int(guess.content) == answear:
            await message.channel.send("You are right!")
        else:
            await message.channel.send("Oops. That is not right")


client.run("ODM3MDExNTQ4MzI4NTU4NjQy.YImVwA.uyVQ37eLymHL2Kt2v76eCbR8GR4")
