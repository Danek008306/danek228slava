from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token= TELEGRAM_TOKEN)
dp = Dispatcher(bot)

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
    await message.answer('Привет брат, я твой первый ЭХО бот')

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
