from function import roll, gamer_choice, bot_choice, check_win
from classes import dices

play = True
list_difficulty = ('Легкая', 'Средняя', 'Тяжелая')

def game(nik):
    print(f'Добро пожаловать в игру "Стихийные кости", дорогой {nik}')
    hp_gamer = 10
    hp_bot = 0
    while hp_bot == 0:
        print('Пожалуйста выберите сложность игры', 'На выбор:', *list_difficulty)
        difficulty = input()

        if difficulty == list_difficulty[0]:
            hp_bot = 5
        elif difficulty == list_difficulty[1]:
            hp_bot = 10
        elif difficulty == list_difficulty[2]:
            hp_bot = 15
        else:
            print('Проверьте правильность написания')


    while hp_bot > 0 and hp_gamer > 0:
        print(f'Ваше здоровье: {hp_gamer}\nЗдоровье соперника: {hp_bot}')
        print('Вы бросаете стихийные кости')

        player_points, bot_points = check_win()
        print(f'Ваши очки: {player_points}\nОчки соперника: {bot_points}')

        if player_points >= bot_points:
            print('Этот раунд за вами, ваш соперник получил урон в размере', player_points)
            hp_bot -= player_points
            if hp_bot <= 0:
                print('Ура! Победа!')
        else:
            print('Этот раунд проигран, Вы получили урон в размере', bot_points)
            hp_gamer -= bot_points
            if hp_gamer <= 0:
                print('Упс! Не повезло!')

