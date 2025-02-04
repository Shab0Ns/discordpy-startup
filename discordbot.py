from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='?')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def neko(ctx):
    await ctx.send('にゃーん')


@bot.command()
async def hello(ctx):
    await ctx.send('にゃーん')

@bot.event()
async def on_message(message):
    if message.content.startswith("こんにちは"):
        if client.user != message.author:
            msg = "こんにちは " + message.author.name + "さん！"
            await client.send_message(message.channel, msg)
@bot.command()
async def 最強(ctx):
    await ctx.send('にゃーん')

bot.run(token)
