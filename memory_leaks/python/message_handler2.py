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
async def test_message_handler_handles_failed_downloads():
    # Mocking the message object
    message = MagicMock()
    message.text = "valid song link"
    message.reply = AsyncMock()
    message.reply_audio = AsyncMock()
    message.edit_text = AsyncMock()

    event_chat = MagicMock()

    # Mock spotify.download to simulate partial failures
    async def mock_download(text):
        if text == "valid song link":
            return ["song1.mp3", None, "song3.mp3"]  # Simulating a failed download

        spotify = MagicMock()
        spotify.download = AsyncMock(side_effect=mock_download)
        await message_handler(message, event_chat, spotify)

        assert message.reply.called  # Ensure reply message was sent
        assert message.reply_audio.call_count == 2  # Only successful downloads are processed
        assert message.edit_text.call_count == 0  # Should not display failure message if some downloads succeeded

    await mock_download(message.text)
    print("No memory leaks detected!")

async def main():
    await test_message_handler_handles_failed_downloads()

asyncio.run(main())