from datetime import date
import telebot
from spreadsheet import add_expense_to_sheet

bot_token = '7130959835:AAE2_9i0vCj6MO2TX-h2YHFug-pvx8Klx9E'
googlesheet_id = '1S4ksOdt7L49XS09Dm1xTxzDWSDD7UsfnKoTPeNigYPg'
bot = telebot.TeleBot('7130959835:AAE2_9i0vCj6MO2TX-h2YHFug-pvx8Klx9E')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,"Привет, Денис. Введи расход через дефис в виде [Категория-Цена-Комментарий]:")

@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    try:
        category, price, comment = message.text.split("-")
        add_expense_to_sheet(googlesheet_id, category, price, comment)
        today = date.today().strftime("%d.%m.%Y")
        text_message = f'На {today} в таблицу расходов добавлена запись: {category} ценой в {price} тенге, {comment} '
        bot.send_message(message.chat.id, text_message)
    except:
        bot.send_message(message.chat.id, 'ОШИБКА! Неправильный формат данных!')

    bot.send_message(message.chat.id, 'Введи расход через дефис в виде [Категория-Цена-Комментарий]:')


if __name__ == '__main__':
    bot.polling(none_stop=True)
