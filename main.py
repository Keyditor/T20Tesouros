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
        await message.reply('$hello!')

    if message.content.startswith('$loot'):
        nd = str(message.content)
        nd = nd.split(" ")
        print(nd)
        try:
            await message.reply(rolls.RollLoot(nd[1]))
        except:
            await message.reply("**Algo está faltando!!**\n Lembre-se de imformar o ND da rolagem de tesouros\n Ex:. $loot **2** | $loot **1/4**")

    if message.content.startswith('$exit'):
        await message.reply("*** ==> CAMBIO E DESLIGO! <== ***")
        exit()

    try:
        text = str(rolls.DiceRoll(message.content))
        if len(text) >= 3999:
            await message.reply(" ***OPS!! Não tenho tantos dados pra fazer essa rolagems =(***")
        else:
            await message.reply(text)
    except:
        pass

tokentxt = open("token.txt","r")
token = tokentxt.read()
print("Token de autenticação:\n",token)
print("Iniciando Tauba Redonda!")

client.run(token)