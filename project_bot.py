import asyncio
import time

from aiogram import Dispatcher
from aiogram import Bot
from aiogram import types
from aiogram.filters.command import Command

from tokentg import BOTTOKEN
from Url_sort import PriceFind


BD=[]




bot = Bot(token=BOTTOKEN)
disp = Dispatcher()

@disp.message(Command("start"))
async def Welcome(message: types.Message):
    await message.answer("""Привет!
                         Этот бот помогает вам отследить цену на товар на различных маркетплейсах 
                         Вам всего лишь нужно выбрать размер подения цены и скинуть ссылку на товар и ждать... 
                         Бот сам отправит вам оповещение когда цена будет выгодной для вас! """)


@disp.message(Command("mylinks"))
async def Links(message: types.Message):
    answer="ваши ссылки на товары:\n"
    for i in BD :
        if message.from_user.id == i[0]:
            namepr = PriceFind(i[1])
            answer+=f"Товар: {namepr[0]} \nцена: {namepr[1]}"
    await message.answer(answer)


@disp.message()
async def Url(message: types.Message):
    name_pr = PriceFind(message.text)
    if PriceFind(message.text) != -1:
        BD.append([message.from_user.id, message.text, 20, PriceFind(message.text)])
        await message.answer(f"Ссылка принята, нынешняя цена на товар:{name_pr[0]} :: {name_pr[1]}\nМы отправим вам уведомление когда цеyа упадет бльше чем 20%\n(значение падения цены вы можете изменить сами командой /percent)")
    else:
        await message.answer("Ссылка не рабочая, измените ссылку и попробуйте снова")




async def main():
    await disp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())
















