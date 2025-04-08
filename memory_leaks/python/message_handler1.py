import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock
from pathlib import Path
from aiogram.types import Chat, FSInputFile, Message, User

async def message_handler(message: Message, event_chat: Chat, spotify) -> None:
    if not message.text or not message.text.startswith(''):
        return None

    bot_message: Message = await message.reply(
        'Downloading music from the link...\nThis process may take a few minutes.'
    )

    songs: list[Path] | None = await spotify.download(message.text)

    if not songs:
        await bot_message.edit_text(
            'Could not find or download music at the link, please try again later or send a different link.'
        )
        return

    for song in songs:
        await message.reply_audio(FSInputFile(song))
    await bot_message.delete()

@pytest.mark.asyncio
async def test_message_handler_no_text():
    message = MagicMock()
    message.text = None  # Simulating missing text
    message.reply = AsyncMock()

    event_chat = MagicMock()

    spotify = MagicMock()
    spotify.download = AsyncMock(return_value=None)

    result = await message_handler(message, event_chat, spotify)

    assert result is None  # Should safely return None instead of crashing
    message.reply.assert_not_called()  # Ensure no message is sent

    print("Checking for no message test passed!")

async def main():
    await test_message_handler_no_text()

asyncio.run(main())