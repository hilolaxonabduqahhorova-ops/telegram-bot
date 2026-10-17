
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


async def asosiy_menyu():
    markup = ReplyKeyboardMarkup(
        
keyboard=[
    [
        KeyboardButton(text="📚 Maktab darsliklari"),
        KeyboardButton(text="🌐 IT Course")
    ],
    [
        KeyboardButton(text="📚 IELTS Course")
    ],
    [
        KeyboardButton(text="📞 Aloqa")
    ]
],
       resize_keyboard=True
    )
    return markup


async def darsliklar_tugmalari():
    tugmalar = []

    for i in range(1, 5):
        tugmalar.append([
            KeyboardButton(text=f"{i}-sinf")
        ])

    tugmalar.append([
        KeyboardButton(text="Go Back")
    ])

    return ReplyKeyboardMarkup(
        keyboard=tugmalar,
    resize_keyboard=True
    )

async def it_tugmalari():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="💻 Dasturlash bo‘yicha qo‘llanma")

            ],
            [
                KeyboardButton(text="Go Back")
            ]
        ],
    resize_keyboard=True
    )

async def ielts_tugmalari():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📖 IELTS haqida qolanma")
            ],
            [
                KeyboardButton(text="Go Back")
            ]
        ],
    resize_keyboard=True

    )

async def tel_tugmalari():
    return ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="📱 Telefon raqamni yuborish",request_contact=True)
            ],
            [
                KeyboardButton(text="📍 Lokatsiyani yuborish",request_location=True)
            ],
            [
                KeyboardButton(text="Go Back")
            ]

        ],
        resize_keyboard=True
    )