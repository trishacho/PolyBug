import pytest
import asyncio
from unittest.mock import AsyncMock, MagicMock
from pathlib import Path
from aiogram.types import FSInputFile
from message_handler import message_handler

@pytest.mark.asyncio
async def test_message_handler():
    # mock message object
    message = AsyncMock()
    message.text = "https://open.spotify.com/track/example"
    message.reply = AsyncMock()
    message.reply_audio = AsyncMock()

    # mock bot message (response to initial user input)
    bot_message = AsyncMock()
    message.reply.return_value = bot_message

    # mock event_chat
    event_chat = MagicMock()

    # simulate fixed function behavior
    spotify = MagicMock()
    spotify.download = AsyncMock(return_value=[Path("/fake/song.mp3")])  # simulate successful download

    # run fixed handler
    await message_handler(message, event_chat, spotify)

    # check that bot message was sent initially
    message.reply.assert_called_once_with(
        'Downloading music from the link...\nThis process may take a few minutes.'
    )

    # ensure reply_audio was called once
    message.reply_audio.assert_called_once()

    # check that argument is an instance of FSInputFile
    arg = message.reply_audio.call_args[0][0]  # Get the first argument of the first call
    assert isinstance(arg, FSInputFile), "Expected FSInputFile instance"

    # check that bot message is deleted after sending the song
    bot_message.delete.assert_called_once()

    print("All song tests passed!")

@pytest.mark.asyncio
async def test_message_handler_no_songs():
    """Test case where no songs are found"""
    message = AsyncMock()
    message.text = "https://open.spotify.com/track/example"
    message.reply = AsyncMock()
    message.reply_audio = AsyncMock()

    bot_message = AsyncMock()
    message.reply.return_value = bot_message

    event_chat = MagicMock()

    # simulate spotify.download returning None
    spotify = MagicMock()
    spotify.download = AsyncMock(return_value=None)

    await message_handler(message, event_chat, spotify)

    # ensure failure message is sent
    bot_message.edit_text.assert_called_once_with(
        'Could not find or download music at the link, please try again later or send a different link.'
    )

    # ensure no audio was sent
    message.reply_audio.assert_not_called()

    # ensure bot message is deleted
    bot_message.delete.assert_not_called()  # message should remain

    print("All no song tests passed!")

async def main():
    await test_message_handler()
    await test_message_handler_no_songs()

asyncio.run(main())