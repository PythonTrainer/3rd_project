import smtplib
import os
from dotenv import load_dotenv


load_dotenv()
LOGIN = os.getenv("LOGIN")
PASSWORD = os.getenv("PASSWORD")

text = """
Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл.
"""

ref_link = r"https://dvmn.org/referrals/R3f7v75zLCgAafgj0Ioo9OnZHfO0PsBhD247NovM/"
friend_name, my_name = 'Mike', 'Roman'
text = text.replace('%website%', ref_link)
text = text.replace('%friend_name%', friend_name)
text = text.replace('%my_name%', my_name)

to_user = 'official.zmushko2929@yandex.ru'

letter = """From: {0}
To: {1}
Subject: Приглашение!
Content-Type: text/plain; charset="UTF-8";
{2}
""".format(LOGIN, to_user, text).encode('UTF-8')

server = smtplib.SMTP_SSL('smtp.yandex.ru:465')
server.login(LOGIN, PASSWORD)
server.sendmail(LOGIN, to_user, letter)
