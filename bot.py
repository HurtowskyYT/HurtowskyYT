from discord import Embed
import requests
from discord.ext import commands

TOKEN = 'ODM2MTQyODYwNDc0NjQ2NTQ4.YIZsuA.Ekw5AAF76ogEM37ZSPYZIr0o1_o'

client = commands.Bot(command_prefix=';')
@client.event
async def on_ready():
    print('Połączono z botem: ()'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))
async def on_message(ping):
    print(f'Pong {message.author.nick}.')

client.remove_command("help")   

@client.command()
async def ping(ctx):
    await ctx.send('Pong :)')
@client.command()
async def help(ctx):
     embed = Embed(title="Pomoc", color=15158332, description="Moderacja```!help moderacja```  4fun```!help 4fun```")
     await ctx.send(embed=embed)
@client.command()
async def help_moderacja(ctx):
     embed = Embed(title="Moderacja", color=15158332, description="W krótce!")
     await ctx.send(embed=embed)
@client.command()
async def help_4fun(ctx):
     embed = Embed(title="4fun", color=15158332, description="Memy```!meme```")
     await ctx.send(embed=embed)
@client.command()
async def meme(ctx):
        r = requests.get('https://ivall.pl/memy')
        json_data = r.json()
        image_url = json_data['url']

        embed = Embed(title="Meme", color=35531)
        embed.set_image(url=image_url)
        embed.set_footer(icon_url=ctx.author.avatar_url, text=f"{ctx.author.name}#{ctx.author.discriminator}")

        await ctx.send(embed=embed)
    
client.run(TOKEN)
