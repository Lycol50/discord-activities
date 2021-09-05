import json
import os
import platform
import random
import sys
from discordTogether import DiscordTogether
import discord
from discord.ext import commands, tasks
from discord.ext.commands import Bot

client = commands.Bot(command_prefix="play ")
togetherControl = DiscordTogether(client)

bot = Bot(command_prefix=["play "], intents=discord.Intents.default())

#youtube
@client.command(aliases=['yt', 'youtub', 'youtube.com'])
async def youtube(ctx):
    if ctx.author.voice == None:

        embed = discord.Embed(
            title="ERROR!",
            description="You need to connect to a vc before you can start youtube",
            color=0xE02B2B
        )

        embed.set_footer(text = "coded by cold#4777 and tram#0001", icon_url = "https://cdn.discordapp.com/avatars/669089379263709184/87b98935dfbaff3d4470df3c21b91a0f")

        await ctx.send(embed=embed)
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'youtube', max_age=60)

    embed = discord.Embed(
        title="Here's your link",
        description=(f"click the link to start youtube \n{link}" + (f'\n{ctx.message.author.mention}') + (' has requested this command \n \n ||this link will expire in 1 minute to save resources and lag||')),
        color=0x69dab4
    )

    embed.set_footer(text = "coded by cold#4777 and tram#0001", icon_url = "https://cdn.discordapp.com/avatars/669089379263709184/87b98935dfbaff3d4470df3c21b91a0f")

    await ctx.send(embed=embed)





#chess
@client.command()
async def chess(ctx):
    if ctx.author.voice == None:

        embed = discord.Embed(
            title="ERROR!",
            description="You need to connect to a vc before you can start chess",
            color=0xE02B2B
        )

        embed.set_footer(text = "coded by cold#4777 and tram#0001", icon_url = "https://cdn.discordapp.com/avatars/669089379263709184/87b98935dfbaff3d4470df3c21b91a0f")

        await ctx.send(embed=embed)
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'chess', max_age=60)

    embed = discord.Embed(
        title="Here's your link",
        description=(f"click the link to start chess \n{link}" + (f'\n{ctx.message.author.mention}') + (' has requested this command \n \n ||this link will expire in 1 minute to save resources and lag||')),
        color=0x69dab4
    )

    embed.set_footer(text = "coded by cold#4777 and tram#0001", icon_url = "https://cdn.discordapp.com/avatars/669089379263709184/87b98935dfbaff3d4470df3c21b91a0f")

    await ctx.send(embed=embed)








#fishington
@client.command(aliases=['fish', 'fishing', 'fishington.io'])
async def fishington(ctx):

    if ctx.author.voice == None:
        embed = discord.Embed(
            title="ERROR!",
            description="You need to connect to a vc before you can play fishington.io",
            color=0xE02B2B
        )

        embed.set_footer(text = "coded by cold#4777 and tram#0001", icon_url = "https://cdn.discordapp.com/avatars/669089379263709184/87b98935dfbaff3d4470df3c21b91a0f")

        await ctx.send(embed=embed)
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'fishing', max_age=60)

    embed = discord.Embed(
        title="Here's your link",
        description=(f"click the link to start fishington.io \n{link}" + (f'\n{ctx.message.author.mention}') + (' has requested this command \n \n ||this link will expire in 1 minute to save resources and lag||')),
        color=0x69dab4
    )

    embed.set_footer(text = "coded by cold#4777 and tram#0001", icon_url = "https://cdn.discordapp.com/avatars/669089379263709184/87b98935dfbaff3d4470df3c21b91a0f")

    await ctx.send(embed=embed)

#poker
@client.command('poke')
async def poker(ctx):

    if ctx.author.voice == None:
        embed = discord.Embed(
            title="ERROR!",
            description="You need to connect to a vc before you can play poker",
            color=0xE02B2B
        )

        embed.set_footer(text = "coded by cold#4777 and tram#0001", icon_url = "https://cdn.discordapp.com/avatars/669089379263709184/87b98935dfbaff3d4470df3c21b91a0f")

        await ctx.send(embed=embed)
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'poker', max_age=60)

    embed = discord.Embed(
        title="Here's your link",
        description=(f"click the link to start poker \n{link}" + (f'\n{ctx.message.author.mention}') + (' has requested this command \n \n ||this link will expire in 1 minute to save resources and lag||')),
        color=0x69dab4
    )

    embed.set_footer(text = "coded by cold#4777 and tram#0001", icon_url = "https://cdn.discordapp.com/avatars/669089379263709184/87b98935dfbaff3d4470df3c21b91a0f")

    await ctx.send(embed=embed)

#betrayal.io
@client.command(aliases=['betrayal.io', 'amongus', 'amogus', 'susus_amogus', 'whats_so_funny_about_susus_amogus', "what's_so_funny_about_susus_amogus"])
async def betrayal(ctx):

    if ctx.author.voice == None:
        embed = discord.Embed(
            title="ERROR!",
            description="You need to connect to a vc before you can play betrayal.io",
            color=0xE02B2B
        )

        embed.set_footer(text = "coded by cold#4777 and tram#0001", icon_url = "https://cdn.discordapp.com/avatars/669089379263709184/87b98935dfbaff3d4470df3c21b91a0f")

        await ctx.send(embed=embed)
    link = await togetherControl.create_link(ctx.author.voice.channel.id, 'betrayal', max_age=60)

    embed = discord.Embed(
        title="Here's your link",
        description=(f"click the link to start betrayal.io \n{link}" + (f'\n{ctx.message.author.mention}') + (' has requested this command \n \n ||this link will expire in 1 minute to save resources and lag||')),
        color=0x69dab4
    )

    embed.set_footer(text = "coded by cold#4777 and tram#0001", icon_url = "https://cdn.discordapp.com/avatars/669089379263709184/87b98935dfbaff3d4470df3c21b91a0f")

    await ctx.send(embed=embed)

client.run("your_token_here")
