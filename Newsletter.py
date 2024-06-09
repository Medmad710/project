import time
from project_bot import BD, bot
from  Url_sort import PriceFind




async def Sale():
    await bot.send_message(chat_id="776214067", text="hihihihihih" )

while True:
    time.sleep(10)
    for list in BD:
        for l in list:
            if PriceFind(l[1]) < l[3]* (1 - l[2]/100):
                message = f"{PriceFind(l[1])}"
                Sale()