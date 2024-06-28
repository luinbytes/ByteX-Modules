import asyncio

from discord.ext import commands, tasks
import discord

class Utilities(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.message.delete()

        # Generate a codeblock with the bot's latency
        message_id = await ctx.send(f"`ByteX's latency is {round(self.bot.latency * 1000)}ms`")

        await asyncio.sleep(5)
        await ctx.channel.delete_messages([message_id])

async def setup(bot):
    await bot.add_cog(Utilities(bot))
