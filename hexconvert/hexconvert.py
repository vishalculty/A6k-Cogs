import discord
import os
import asyncio

from discord.ext import commands
from cogs.utils.dataIO import fileIO
from cogs.utils.chat_formatting import *
from __main__ import send_cmd_help

class Convert(object):
    def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
        bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
        return bits.zfill(8 * ((len(bits) + 7) // 8))

    def text_from_bits(bits, encoding='utf-8', errors='surrogatepass'):
        n = int(bits, 2)
        return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'
    
class Hexconvert(object)
    def __init__(self, bot):
        self.bot = bot
        self.convert = Convert()
    
    @commands.group(pass_context=True)
    async def hexconvert(self, ctx):
        """Convert Hex to ASCII, or ASCII to Hex"""
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
    
    @Hexconvert.command(pass_context=True, name="toascii")
    async def _toascii(self, ctx, hexadecimal: str):
    """Convert an appended Hex string to ASCII. If there are spaces in the Hex string it must be encased in quotes."""
        await self.bot.say(self.convert.text_from_bits(hexadecimal))
    
    @Hexconvert.command(pass_context=True, name="tohex")
    async def _tohex(self, ctx, ascii: str):
    """Convert an appended ASCII string to Hex. If there are spaces in the ASCII string it must be encased in quotes."""
        await self.bot.say(self.convert.text_to_bits(ascii))
    
def setup(bot):
    n = Hexconvert(bot)
    bot.add_cog(n)