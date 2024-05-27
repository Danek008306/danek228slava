from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=2)
    but_inline = InlineKeyboardButton('Посмотреть', url='ru.wikipedia.org')
    but_inline2 = InlineKeyboardButton('Посмотреть', url='ru.wikipedia.org')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline
