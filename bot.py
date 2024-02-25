import discord
from discord.ext import commands

# Creează un obiect intents
intents = discord.Intents.default()

# Activează evenimentele de mesaje și alte evenimente pe care le dorești
intents.message_content = True
# Adaugă și alte evenimente aici, dacă este necesar

# Creează instanța Client cu intents
bot = commands.Bot(command_prefix="/", intents=intents)

# Restul codului rămâne neschimbat
@bot.event
async def on_ready():
    print(f'Botul este conectat ca {bot.user}')

@bot.event
async def on_message(message):
    # Verifică dacă mesajul este pe canalul specific
    if message.channel.id == 1210709521362587718 and message.content == '/gen1':
        # Trimite mesajul pe canal
        await message.channel.send('salut mita')
        # Trimite mesaj privat către utilizator
        await message.author.send('merge')

# Conectează botul folosind token-ul
bot.run('MTIxMTQwNjYwMDc4NzczMDUxMg.Gsd8rY.6HQUGeSUwrrprbL7LdzvMMgGcD_BHsJBaAzbEU')