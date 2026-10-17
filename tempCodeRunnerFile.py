import asyncio
from aiogram import Bot,Dispatcher,F
from aiogram.filters import Command
from aiogram.types import Message,FSInputFile

from buttons import asosiy_menyu,darsliklar_tugmalari,it_tugmalari,ielts_tugmalari,tel_tugmalari

bot=Bot(token="8263056378:AAFRmq1H3WmzjtXcUETDGDJOHq8GVkp0WvI")
dp=Dispatcher()

@dp.message(Command('start'))
async def start(message:Message):
    await message.answer("assalomu alaykum botga xuw kelibsiz 😇",reply_markup=await asosiy_menyu())

@dp.message(F.text=="📚 Maktab darsliklari")
async def maktab_darsliklari(message:Message):
    await message.answer("sinfni tanlang!",reply_markup=await darsliklar_tugmalari())

@dp.message(F.text=="1-sinf")
async def birinci_sinf(message:Message):
    rasm=FSInputFile("muwuk..webp")
    await message.answer_photo(photo=rasm)


@dp.message(F.text=="🌐 IT Course")
async def it_course(message:Message):
    await message.answer("IT Course bolimini tanlang!",reply_markup=await it_tugmalari())


@dp.message(F.text=="💻 Dasturlash bo‘yicha qo‘llanma") 
async def dalsturlaw_qollanma(message:Message):
    hujt1=FSInputFile("hujat1.txt")
    hujt2=FSInputFile("hujat2.txt")

    await message.answer_document(hujt1)
    await message.answer_document(hujt2)


@dp.message(F.text=="📚 IELTS Course")
async def ielt_course(message:Message):
    await message.answer("IELTS qo‘llanma bolimini tanlang!",reply_markup=await ielts_tugmalari())

@dp.message(F.text=="📖 IELTS haqida qolanma")
async def ielts_qollannm(message:Message):
    hujt=FSInputFile("ielts.txt")

    await message.answer_document(hujt)

@dp.message(F.text == "📞 Aloqa")
async def aloqa(message: Message):
    await message.answer(
        "Telefon raqami yoki lokatsiyani yuboring!",
        reply_markup=await tel_tugmalari()
    )

@dp.message(F.contact)
async def kontakt_qabul(message: Message):
    await message.answer(
        f"Telefon raqamingiz: {message.contact.phone_number}"
    )
@dp.message(F.location)
async def lokatsiya_qabul(message: Message):
    lat = message.location.latitude
    lon = message.location.longitude

    await message.answer(
        f"Lokatsiyangiz qabul qilindi!\n"
        f"Latitude: {lat}\n"
        f"Longitude: {lon}"
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
