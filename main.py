from datetime import date
import telebot
import gspread

bot_token = '7130959835:AAE2_9i0vCj6MO2TX-h2YHFug-pvx8Klx9E'
googlesheet_id = '1S4ksOdt7L49XS09Dm1xTxzDWSDD7UsfnKoTPeNigYPg'
bot = telebot.TeleBot('7130959835:AAE2_9i0vCj6MO2TX-h2YHFug-pvx8Klx9E')
gc = gspread.service_account()


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message,"Привет, Денис. Введи расход через дефис в виде [Категория-Цена-Комментарий]:")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    try:
        today = date.today().strftime("%d.%m.%Y")

        category, price, comment = message.text.split("-")
        text_message = f'На {today} в таблицу расходов добавлена запись: {category} ценой в {price} тенге, {comment} '
        bot.send_message(message.chat.id, text_message)

        sh = gc.open_by_key(googlesheet_id)
        sh.sheet1.append_row([today, category, price, comment])
    except:
        bot.send_message(message.chat.id, 'ОШИБКА! Неправильный формат данных!')

    bot.send_message(message.chat.id, 'Введите расход через дефис в виде [Категория-Цена-Комментарий]:')


if __name__ == '__main__':
    bot.polling(none_stop=True)