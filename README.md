# LurajBot

An early Discord bot project with server information, latency, jokes, memes, quotes and a number-guessing game. Commands use the `.l ` prefix.

## Local setup

Use Python 3.10 or newer and a Discord bot account. Enable **Message Content Intent** in the Discord Developer Portal so prefix commands can read messages. Invite the bot with permission to view its channels, send messages and embed links.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
read -rsp 'Discord bot token: ' DISCORD_BOT_TOKEN
export DISCORD_BOT_TOKEN
python LurajBot.py
```

The token is read from the environment. Keep it out of source files and commit history.

## Commands

| Command | Purpose |
|---|---|
| `.l server` | Show server information, inside a server |
| `.l hi` | Send a greeting |
| `.l ping` | Show gateway latency |
| `.l joke` | Send a programming joke |
| `.l meme` | Request a meme using pyrandmeme |
| `.l guess` | Guess a number within 30 seconds |
| `.l quotes` | Send a quote from the local collection |

## Status

A learning project with a modernization patch for discord.py 2.x. The original 1.7-era API calls have been replaced, token loading uses an environment variable, and guesses are scoped to the initiating user and channel. Live Discord login and third-party meme availability have not been checked for this patch. The bot has no persistent storage or moderation features.

API migration reference: [discord.py migration guide](https://discordpy.readthedocs.io/en/stable/migrating.html).
