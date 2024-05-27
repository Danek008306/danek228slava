from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN
from fafa import get_keyboard_1, get_keyboard_2
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

keyboard_inline = InlineKeyboardMarkup(row_width= 2)
but_inline = InlineKeyboardButton('Посмотреть', url= 'ru.wikipedia.org')
but_inline2 = InlineKeyboardButton('Посмотреть', url= 'ru.wikipedia.org')
keyboard_inline.add(but_inline, but_inline2)


async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command='/start', description= 'Команда для запуска бота'),
        types.BotCommand(command='/help', description='Команда для помощи'),
        types.BotCommand(command='/clear', description='Команда для очистки чата'),
        types.BotCommand(command='/friend', description='Команда для дружбы с ботом'),
        types.BotCommand(command='/unfriend', description='Команда для ссоры с ботом'),
    ]

    await bot.set_my_commands(commands)



@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.answer('Привет брат, я твой первый ЭХО бот', reply_markup= get_keyboard_1())

@dp.message_handler(lambda message: message.text == 'Отправь фото машины')
async def button_1_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://avatars.mds.yandex.net/i?id=19699e2977a218c19ae95f8a064bb23433d465e5-10698550-images-thumbs&n=13', caption= 'Вот, тебя показал', reply_markup= keyboard_inline)

@dp.message_handler(lambda message: message.text == 'Перейти на следующую клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить отправить фото мотоцикла', reply_markup= get_keyboard_2())

@dp.message_handler(lambda message: message.text == 'Отправь фото мотоцикла')
async def button_3_click(message: types.Message):
    await bot.send_photo(message.chat.id, photo= 'https://avatars.mds.yandex.net/i?id=79e2c781d739e1c91e927f5c881d5d2bab5b2d3f-12923554-images-thumbs&n=13', caption= 'Вот, показал твоего друга')

@dp.message_handler(lambda message: message.text == 'Вернуться на 1 клавиатуру')
async def button_2_click(message: types.Message):
    await message.answer('Тут ты можешь попросить отправить фото машины', reply_markup= get_keyboard_1())
@dp.message_handler(commands= 'help')
async def help(message: types.Message):
    await message.answer('Ты знаешь где меня искать, могу помочь с ....')

@dp.message_handler(commands= 'clear')
async def clear(message: types.Message):
    await message.answer('Брат, мы начинаем с чистого листа')

@dp.message_handler(commands='friend')
async def friend(message: types.Message):
    await message.answer('Теперь мы братья')

@dp.message_handler(commands='unfriend')
async def unfriend(message: types.Message):
    await message.answer('Не брат ты мне больше')


@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates= True, on_startup= on_startup)
