import pytest
from unittest.mock import AsyncMock, MagicMock
from message_handler import message_handler

@pytest.mark.asyncio
async def test_message_handler_no_text():
    message = MagicMock()
    message.text = None  # simulating missing text
    message.reply = AsyncMock()

    event_chat = MagicMock()

    spotify = MagicMock()
    spotify.download = AsyncMock(return_value=None)

    result = await message_handler(message, event_chat, spotify)

    assert result is None  # should return None instead of crashing
    message.reply.assert_not_called()  # ensure no message is sent

    print("Checking for no message test passed!")