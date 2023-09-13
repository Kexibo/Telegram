"""All configs for app."""
from os import getenv
from dotenv import load_dotenv


load_dotenv()
# Токен бота
BOT_TOKEN = getenv('BOT_TOKEN')
# Логин и пароль прогеров
prog_login = getenv('prog_login')
prog_password = getenv('prog_password')
# Логин и пароль инфобезников
infsec_login = getenv('infsec_login')
infsec_password = getenv('infsec_password')
# Основной url для запроса расписания
main_url = 'https://lks.siriusuniversity.ru/schedule/groups'
# Куда вводить логин и пароль расписания
login_str = '/html/body/div[2]/div/div/div[2]/div/form/div[4]/input'
password_str = '/html/body/div[2]/div/div/div[2]/div/form/div[5]/input'
days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
max_lessons = 6
# Куда кешируется расписание
progs_file = 'prog.txt'
infsec_file = 'infsec.txt'

greet = "Привет я не готовое говно, меня надо написать️"
menu = "📍 Главное меню"
gen_exit = "Чтобы выйти из диалога нажмите на кнопку ниже"
gen_wait = "⏳Пожалуйста, подождите немного, пока нейросеть обрабатывает ваш запрос..."
text_watermark = '\n_______________________________________\nСоздано при помощи @dalle_chatgpt_bot'
gen_error = f'🚫 Ошибка генерации. Возможные причины:\n1. Перегружены сервера OpenAI\n2. Ваш запрос нарушил правила OpenAI\n3. Ошибка в работе бота\nЕсли вы считаете, что проблема вызвана неисправностью бота, сообщите админу'

