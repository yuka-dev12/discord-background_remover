import discord
import os
from dotenv import load_dotenv
from remover import remover
from discord.ext import commands

os.makedirs("tmp", exist_ok=True)
intents = discord.Intents.all()
client = commands.Bot(command_prefix='.', intents=intents)

@client.event
async def on_ready():
    print(f"Bot is online as {client.user}!")

@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! Took **{round(client.latency * 1000)}** ms to respond.")

@client.command()
async def bgr(ctx):
    if not ctx.message.attachments:
        await ctx.send("Attach an image too remove the background!")
        return
    attachment = ctx.message.attachments[0]
    if not attachment.content_type.startswith('image/'):
        await ctx.send("Attach image file type!")
        return
    await attachment.save(f"tmp/raw.png")

    remover("tmp/raw.png")
    file = open(f"tmp/removed.png", "rb")
    removed_img = discord.File(file)
    await ctx.send(file=removed_img)
    file.close()

    
if __name__ == "__main__":
    load_dotenv()
    Token = os.getenv('Bot-token')
    client.run(Token)