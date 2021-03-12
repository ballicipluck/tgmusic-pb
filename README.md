# Telegram VC Music Player 
### Open-Sourced PyTgCalls based Pyrogram bot to play music in Voice Chats
---
## Note

Neither this, or PyTgCalls are fully stable.

## Requirements

- FFmpeg
- NodeJS [nodesource.com](https://nodesource.com/)
- Python 3.7+
- [PyTgCalls](https://github.com/pytgcalls/pytgcalls)

### Credits
[Mayank](https://github.com/hackelite01)  - "Owner"

[#ItsMe.](https://github.com/ballicipluck)

## Deployment

### Config

- Copy `example.env` to `.env` and fill it with your credentials.

- If you don't already have it, Generate the string session by running this script locally. Or you can use bots like `@StringSessionGen_Bot` on Telegram.
```
# First install Pyrogram with:
# pip install Pyrogram TgCrypto
from pyrogram import Client
api_id = int(input('Enter your API ID: '))
api_hash = input('Enter API HASH')
with Client(":memory:", api_id, api_hash) as app, open("session.txt", "w+") as s_file:
    session_string = app.export_session_string()
    s_file.write(session_string)
    print("Session string has been saved to session.txt")
    print(session_string)
```
<!---
### Without Docker
1. Install Python requirements:
   ```bash
   pip install -r requirements.txt
   ```
2. Run:
   ```bash
   python main.py
   ```
### Using Docker
1. Build:
   ```bash
   docker build -t musicplayer .
   ```
2. Run:
   ```bash
   docker run --env-file .env musicplayer
   ```
--->
### Heroku
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/hackelite01/TgGroupMusicVcBot/)

## After Deploying
- Add the bot and the user(whose `SESSION_STRING` you used) to the group with admin privilages and start a voice chat manually once and leave it. (Don't end it).
- Remember, If you try to enter the Voice Chat from the same user's account(whose `SESSION_STRING` you used), you will stop the music.
- So, better login to a different account and enter the voice chat to hear the music.

 ## Join [Mayank](https://github.com/hackelite01) on Telegram

<a href="https://t.me/hackelite01"><img src="https://img.shields.io/badge/Join-Telegram%20Channel-red.svg?logo=Telegram" width="190" height="28"></a>
