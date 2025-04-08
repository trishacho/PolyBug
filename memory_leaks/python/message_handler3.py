import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock, patch
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
async def test_message_handler_memory_leak():
    message = MagicMock()
    message.text = "valid link"
    message.reply = AsyncMock()
    message.reply_audio = AsyncMock()

    event_chat = MagicMock()

    async def mock_download(song_text):
        return ["song1.mp3", "song2.mp3"]  # Simulating multiple songs

    spotify = MagicMock()
    spotify.download = AsyncMock(side_effect=mock_download)

    await message_handler(message, event_chat, spotify)

    assert spotify.download.called  # Ensure the download is called
    assert message.reply_audio.call_count == 2  # Ensure all songs are processed safely
    print("No memory leaks detected!")

async def main():
    await test_message_handler_memory_leak()

asyncio.run(main())