import rolls, discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        print(message.content)
        await message.channel.send('$hello!')

    if message.content.startswith('$loot'):
        nd = str(message.content)
        nd = nd.split(" ")
        print(nd)
        try:
            await message.channel.send(rolls.RollLoot(nd[1]))
        except:
            await message.channel.send("**Algo está faltando!!**\n Lembre-se de imformar o ND da rolagem de tesouros\n Ex:. $loot **2** | $loot **1/4**")


    try:
        text = str(rolls.DiceRoll(message.content))
        if len(text) >= 3999:
            await message.channel.send(" ***OPS!! Não tenho tantos dados pra fazer essa rolagems =(***")
        else:
            await message.channel.send(text)
    except:
        pass


client.run('OTMzODk1NDkyMzI3MzQyMTQx.G1imgh.TgBc9QQKbxPAh20Y-00Ls8aVO_zAsgkqo9q0y4')