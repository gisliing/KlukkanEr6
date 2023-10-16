# Klukkan Er 6
A Discord bot which visits voice channels and announces it's 6 o'clock.

Add your DISCORD_TOKEN into a .env file and assign privilege to your Discord Server.

Requires Python 3.10, discord.py[voice], pynacl and python_dotenv. Developed and deployed on a Raspberry Pi.

Add these lines to Crontab:

00 18 * * * /usr/local/bin/python3.10 /home/pi/KlukkanEr6/bot.py >> /home/pi/KlukkanEr6/bot.log
00 06 * * * /usr/local/bin/python3.10 /home/pi/KlukkanEr6/bot.py >> /home/pi/KlukkanEr6/bot.log
