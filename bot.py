# bot.py
import os, os.path
import random
import time
import discord
from dotenv import load_dotenv
import asyncio
import sys

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
	print(f'{client.user.name} has connected to Discord!')
	await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the time"))
	path, dirs, files = next(os.walk("audio"))
	file_count = len(files)
	for guild in client.guilds:
		for voice_channel in guild.voice_channels:
			if len(voice_channel.voice_states.keys()) > 0:
				print("Connecting to voice channel {}".format(voice_channel))
				vc = await voice_channel.connect()
				audio_file = "audio/{}".format(files[random.randint(1, len(files)-1)])
				print("Playing audio file {}".format(audio_file))
				vc.play(discord.FFmpegPCMAudio(executable="ffmpeg", source=audio_file))
				while vc.is_playing():
					await asyncio.sleep(1)
				await vc.disconnect()
				print("Disconnected from voice channel {}".format(voice_channel))
				sys.exit(0)

client.run(token)