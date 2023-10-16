# Klukkan Er 6
A Discord bot which visits voice channels and announces it's 6 o'clock.

Developed and deployed on a Raspberry Pi. Add your own .wav audio files into /audio to be played at random. Add your DISCORD_TOKEN into a .env file and assign privilege to your Discord Server.

Add these lines to Crontab:
```
00 18 * * * /usr/local/bin/python3.10 /home/pi/KlukkanEr6/bot.py >> /home/pi/KlukkanEr6/bot.log
00 06 * * * /usr/local/bin/python3.10 /home/pi/KlukkanEr6/bot.py >> /home/pi/KlukkanEr6/bot.log
```

## ⭐ Prerequisites
* Python 3.10
* discord.py[voice]
* PyNaCl
* python_dotenv.

## 🤝 Contributors
* Plöntu Pabbi (Hjalti)
