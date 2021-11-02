from discord.ext import commands
import discord
import time
from datecog import setup_date
import asyncio
from discord.ext.commands import AutoShardedBot
from discord.ext.commands import CommandNotFound
bot = commands.AutoShardedBot(shard_count = 4, command_prefix = "m.", case_insensitive = True, help_command = None)
bot_token = "ODYxNjI4MDAwMjI3MTY0MTkw.YOMjmw.It8DQonmTjOI_WInGA6kTHPJBPk"
async def on_ready():
    print(bot.user)

setup_date(bot)
go_on = True
@bot.listen()
async def on_message(message):
    if message.channel.id not in [894832773821517874]:
        return
    if message.author.id != 861628000227164190:
        return
    if not message.embeds:
        return
    if "Solution" not in message.embeds[0].title:
        return
    def check_rl(reaction,user):
        return str(reaction.emoji) == "📵" and reaction.message.id == message.id and bot.user != user
    await message.add_reaction("📵")
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout = 120 ,check = check_rl)
    except:
        return
    rep = message.embeds[0].description
    uid = user.id
    await message.channel.send(f"<@{uid}>\n{rep}")
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error
bot.run(bot_token, reconnect = True)
