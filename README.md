# LurajBot

My first coding project started in eighth grade: I wanted to turn a friend into a Discord bot as a joke for our server.

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

A learning project modernized for discord.py 2.x. The original 1.7-era API calls have been replaced, token loading uses an environment variable, and guesses are scoped to the initiating user and channel. Eight offline command checks passed on 4 October 2026 with Python 3.14 and discord.py 2.7.1. They cover greetings, local quotes, mocked jokes/memes, server information, guessing outcomes, timeout and user/channel input isolation. Live Discord login and third-party meme availability have not been checked. The bot has no persistent storage or moderation features.

API migration reference: [discord.py migration guide](https://discordpy.readthedocs.io/en/stable/migrating.html).

## Offline checks

```sh
python -m unittest -v
```

The tests use mocked command contexts and service responses. They need no bot token and send no Discord messages. Guesses accept only ordinary decimal strings from 1 through 10; unrelated messages, superscript digits and oversized numbers are ignored.
