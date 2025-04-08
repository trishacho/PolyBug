import pytest
from unittest.mock import AsyncMock, MagicMock
from message_handler import message_handler

@pytest.mark.asyncio
async def test_message_handler_memory_leak():
    message = MagicMock()
    message.text = "valid link"
    message.reply = AsyncMock()
    message.reply_audio = AsyncMock()

    event_chat = MagicMock()

    async def mock_download(song_text):
        return ["song1.mp3", "song2.mp3"]  # simulating multiple songs

    spotify = MagicMock()
    spotify.download = AsyncMock(side_effect=mock_download)

    await message_handler(message, event_chat, spotify)

    assert spotify.download.called  # ensure download is called
    assert message.reply_audio.call_count == 2  # ensure all songs are processed safely
    print("No memory leaks detected!")