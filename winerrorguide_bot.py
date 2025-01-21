import telebot

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на токен вашего бота
TOKEN = 'token'

# Путь к файлу с кодами ошибок
ERROR_CODES_FILE = 'error_codes.txt'

# Инициализация бота
bot = telebot.TeleBot(TOKEN)

# Чтение кодов ошибок из файла
error_codes = {}
with open(ERROR_CODES_FILE, 'r', encoding='utf-8') as file:
    for line in file:
        code, description = map(str.strip, line.split(':', 1))
        error_codes[code] = description

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def handle_start(message):
    bot.send_message(message.chat.id, 'Привет! Я бот для расшифровки кодов ошибок Windows 10. Просто отправь мне код ошибки.')

# Обработчик команды /help
@bot.message_handler(commands=['help'])
def handle_help(message):
    bot.send_message(message.chat.id, 'Отправьте мне код ошибки Windows 10, и я предоставлю расшифровку.')

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    input_code = message.text.strip()

    # Поиск расшифровки для кода ошибки
    error_description = error_codes.get(input_code, 'Расшифровка не найдена.')

    # Отправка расшифровки обратно пользователю
    bot.send_message(message.chat.id, f'Код ошибки: {input_code}\nРасшифровка: {error_description}')

# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)
