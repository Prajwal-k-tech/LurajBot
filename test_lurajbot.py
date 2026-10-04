"""Offline command checks: no token, Discord login or outgoing messages."""
import asyncio
import unittest
from types import SimpleNamespace
from unittest.mock import AsyncMock, patch
import LurajBot as bot


class CommandChecks(unittest.IsolatedAsyncioTestCase):
    def context(self):
        return SimpleNamespace(author=object(), channel=object(), send=AsyncMock())

    async def test_greeting(self):
        ctx = self.context()
        await bot.hi.callback(ctx)
        ctx.send.assert_awaited_once_with("Hi im Luraj")

    async def test_quote_is_from_collection(self):
        ctx = self.context()
        await bot.quotes.callback(ctx)
        self.assertIn(ctx.send.await_args.args[0], bot.quotes_1)

    async def test_joke(self):
        ctx = self.context()
        with patch.object(bot.pyjokes, "get_joke", return_value="sample joke"):
            await bot.joke.callback(ctx)
        ctx.send.assert_awaited_once_with("sample joke")

    async def test_meme_uses_embed(self):
        ctx = self.context()
        embed = bot.discord.Embed(title="sample")
        with patch.object(bot, "pyrandmeme", AsyncMock(return_value=embed)):
            await bot.meme.callback(ctx)
        ctx.send.assert_awaited_once_with(embed=embed)

    async def test_server_without_icon(self):
        ctx = self.context()
        ctx.guild = SimpleNamespace(name="Test guild", icon=None, owner=None, owner_id=1, id=2, member_count=3)
        await bot.server.callback(ctx)
        embed = ctx.send.await_args.kwargs["embed"]
        self.assertEqual(embed.title, "Test guild Server Information")
        self.assertEqual(len(embed.fields), 3)

    async def test_guess_scoping_and_input(self):
        ctx = self.context()
        async def wait_for(event, *, check, timeout):
            self.assertEqual(event, "message")
            self.assertEqual(timeout, 30)
            message = lambda value, author=ctx.author, channel=ctx.channel: SimpleNamespace(content=value, author=author, channel=channel)
            self.assertFalse(check(message("4", author=object())))
            self.assertFalse(check(message("4", channel=object())))
            for value in ["0", "11", "no", "²", "4" * 5000]:
                self.assertFalse(check(message(value)))
            self.assertTrue(check(message("10")))
            return message("4")
        with patch.object(bot.client, "wait_for", wait_for), patch.object(bot.random, "randint", return_value=4):
            await bot.guess.callback(ctx)
        self.assertEqual(ctx.send.await_args.args[0], "Correct!")

    async def test_guess_wrong_answer(self):
        ctx = self.context()
        with patch.object(bot.client, "wait_for", AsyncMock(return_value=SimpleNamespace(content="3"))), patch.object(bot.random, "randint", return_value=4):
            await bot.guess.callback(ctx)
        self.assertEqual(ctx.send.await_args.args[0], "The answer was 4.")

    async def test_guess_timeout(self):
        ctx = self.context()
        with patch.object(bot.client, "wait_for", AsyncMock(side_effect=asyncio.TimeoutError)):
            await bot.guess.callback(ctx)
        self.assertIn("Time expired", ctx.send.await_args.args[0])


if __name__ == "__main__":
    unittest.main()
