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
@bot.listen()
async def on_message(message):
    if message.channel.id not in [894832773821517874
        return
    if message.author.id != 861628000227164190:
        return
    if not message.embeds:
        return
    if "Solution" not in message.embeds[0].title:
        return
    def check_rl(reaction,user):
        return str(reaction.emoji) == "📵" and reaction.message.id == message.id and bot.user != user and user.id == int(message.content.strip("<@").strip(">")) 
    await message.add_reaction("📵")
    try:
        reaction, user = await bot.wait_for('reaction_add', timeout = 120 ,check = check_rl)
    except:
        return
    rep = message.embeds[0].description
    uid = user.id
    await message.channel.send(f"<@{uid}>\n{rep}")

@bot.listen()
async def on_message(message):
    if message.channel.id not in [894832773821517874]:
        return
    if not message.embeds:
        return
    if "Solution" not in message.embeds[0].title:
        return
    if message.author.id != 861628000227164190:
        return
    def check_rm(reactionl,userl):
        return str(reactionl.emoji) == "🔔" and reactionl.message.id == message.id and bot.user != userl and userl.id == int(message.content.strip("<@").strip(">"))
    await message.add_reaction("🔔")
    try:
        reactionl, userl = await bot.wait_for('reaction_add', timeout = 120, check = check_rm)
    except:
        return
    footer = message.embeds[0].footer
    footer = str(footer)
    flist = footer.split("|")
    carddetail = flist[1].split("'")
    dm_msg = f"The **{carddetail[0]}** is ready to data"
    await message.channel.send(f"<@{userl.id}> alright I will DM you when date is available for **{carddetail[0]}**")
    await asyncio.sleep(36000)
    await userl.send(dm_msg)
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        return
    raise error
bot.run(bot_token, reconnect = True)
