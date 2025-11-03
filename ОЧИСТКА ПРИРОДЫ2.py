import telebot
import random

BOT_TOKEN = "8376715969:AAE8MMPKxw-lqIfp_D9Ob6VASW9YV5jH0x0"

GREETING_MESSAGE = "Привет! 👋 Я бот, который напоминает о важности чистоты природы. Нажми на кнопку ниже, чтобы получить вдохновляющее сообщение и сделать наш мир чуточку лучше! 🌍"
BUTTON_TEXT = "Сделаем мир чище! ✨"
ECO_PHRASES = [
    "Очистка природы - это не просто уборка а забота о будущем поколении! 🌱",
    "Давайте вместе сделаем мир чище присоединившись к акции по очистке природы! 🤝",
    "Очистка природы - это вклад каждого в сохранение здоровья планеты! 💚",
    "Пусть каждая уборка будет шагом к более зеленому и здоровому миру! 🌳",
    "Чистая планета - счастливое будущее присоединяйся к нам! 🦋",
    "Сделаем наш мир ярче убирая мусор вместе! ☀️",
    "Каждое действие имеет значение твоя забота о природе бесценна! 💧",
]
DEFAULT_RESPONSE = "Нажми на кнопку, чтобы получить новое сообщение!"

bot = telebot.TeleBot(BOT_TOKEN)

def create_main_keyboard():
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(telebot.types.KeyboardButton(BUTTON_TEXT))
    return keyboard

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    keyboard = create_main_keyboard()
    bot.send_message(message.chat.id, GREETING_MESSAGE, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == BUTTON_TEXT)
def handle_eco_button(message):
    random_phrase = random.choice(ECO_PHRASES)
    bot.send_message(message.chat.id, random_phrase, reply_markup=create_main_keyboard())

@bot.message_handler(content_types=['text'])
def handle_other_text(message):
    bot.send_message(message.chat.id, DEFAULT_RESPONSE, reply_markup=create_main_keyboard())

if __name__ == '__main__':
    print("Бот запущен!")
    bot.polling(none_stop=True)

