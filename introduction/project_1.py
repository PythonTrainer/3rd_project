# 19:20 08.04.2023

name_assistant = 'Линда'
print(f"Я твой ассистент, меня зовут {name_assistant}")
user_name = input('Как мне к тебе обращаться?: ')
print(f"Приятно познакомиться, {user_name}")
age_user = int(input('Теперь я знаю, как тебя зовут. А сколько тебе лет?: '))
print(f'Ого, ты взрослый человек. Представляешь, через 10 лет тебе будет {age_user + 10} лет')
rise_user = float(input('Введите свой рост: '))
rise_assistant = 0.53
print(f'Да, уж, ты очень высокий человек, я всего лишь {rise_assistant}! '
      f'Получается ты выше меня на {rise_user - rise_assistant}')
print(f"Я столько всего о тебе узнала! Я в восторге! Тебя зовут {user_name}, "
      f"сейчас тебе {age_user} лет и твой рост {rise_user}")

actions = """Тебе уже не терпится узнать что я умею? Вот список того, чем я могу помочь:
1. Поднять настроение!
2. Напоминть когда кормить кота!
3. Рассказать про лучшее место на земле!
"""
user_answer = int(input(f"{actions}\nСделай выбор: "))

if user_answer == 1:
    print("""Отличный способ за 5 минут улучшить настроение - побаловать себя любимым напитком.
Это может быть зеленый или черный чай, кофе, какао.""")
elif user_answer == 2:
    cat_age = int(input('Выберите возраст кошки:'
                        '1. До года'
                        '2. Больше года'
                        'Введите выбор'))
    if cat_age == 1:
        print("""Котят до года следует кормить несколько раз в сутки: в 2-3 месяца - пять раз в день, 
        в 4-5 месяцев - четыре раза, в 6-12 месяцев - три раза.""")
    elif cat_age == 2:
        print('Такой информацией я не располагаю.')
    else:
        print(f"{user_name}, я Вас не поняла.")
elif user_answer == 3:
    print(f'Лучшее место на земле,{user_name}, там, где твоя семья')
else:
    print('Упс, что-то пошло не так!')