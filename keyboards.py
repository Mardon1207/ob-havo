from telegram import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

WELCOME_KEYBOARD=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Andijon",callback_data="and"),
            InlineKeyboardButton(text="Buxoro",callback_data="bux")
        ],
        [
            InlineKeyboardButton(text="Farg'ona", callback_data="far"),
            InlineKeyboardButton(text="Jizzax", callback_data="jiz")
        ],
        [
            InlineKeyboardButton(text="Namangan",callback_data="nam"),
            InlineKeyboardButton(text="Navoiy", callback_data="nav")
        ],
        [
            InlineKeyboardButton(text="Qashqadaryo", callback_data="qash"),
            InlineKeyboardButton(text="Samarqand",callback_data="sam")
        ],
        [
            InlineKeyboardButton(text="Sirdaryo",callback_data="sir"),
            InlineKeyboardButton(text="Surxondaryo",callback_data="sur")
        ],
        [
            InlineKeyboardButton(text="Toshkent", callback_data="tosh"),
            InlineKeyboardButton(text="Xorazm", callback_data="xor")
        ],
    ]
)

MAIN_KEYBOARD=ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="⛅️ Hozirgi ob-havo"),
            KeyboardButton(text="🗓 Haftalik ob-havo")
        ],
        [
            KeyboardButton(text="📍 Hududni o'zgartirish"),
            KeyboardButton(text="📞 Aloqa")
        ]
    ]
)