from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hi {message.from_user.first_name}!</b>

I am Voice Chat Music Bot, an Open-Source bot that lets you play music in your Telegram groups.
"""
        # reply_markup=InlineKeyboardMarkup(
        #     [
        #         [
        #             InlineKeyboardButton(
        #                 "Source code", url="https://t.me/hackelitebotsupport"
        #             )
        #         ],
        #         [
        #             InlineKeyboardButton(
        #                 "Report", url="https://t.me/mayank_ka_b_for_bot"
        #             ),
        #             InlineKeyboardButton(
        #                 "Channel for more", url="https://t.me/hackelitebotsupport"
        #             )
        #         ]
        #     ]
        # )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No", callback_data="close"
                    )
                ]
            ]
        )
    )
