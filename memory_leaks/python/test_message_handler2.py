import pytest
from unittest.mock import AsyncMock, MagicMock
from message_handler import message_handler

@pytest.mark.asyncio
async def test_message_handler_handles_failed_downloads():
    # mock the message object
    message = MagicMock()
    message.text = "valid song link"
    message.reply = AsyncMock()
    message.reply_audio = AsyncMock()
    message.edit_text = AsyncMock()

    event_chat = MagicMock()

    # mock spotify.download to simulate failed downloads
    async def mock_download(text):
        if text == "valid song link":
            return None

    spotify = MagicMock()
    spotify.download = AsyncMock(side_effect=mock_download)
    await message_handler(message, event_chat, spotify)

    # check that bot message was sent
    message.reply.assert_called_once_with(
        'Downloading music from the link...\nThis process may take a few minutes.'
    )

    # check that bot message was edited with a failure message
    message.reply.return_value.edit_text.assert_called_once_with(
        'Could not find or download music at the link, please try again later or send a different link.'
    )

    # check no songs were sent as audio files
    assert message.reply_audio.call_count == 0