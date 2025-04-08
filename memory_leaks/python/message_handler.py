from pathlib import Path
from aiogram.types import Message, Chat, FSInputFile

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
