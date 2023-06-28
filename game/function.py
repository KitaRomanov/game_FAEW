import random

from classes import dices


# Бросок костей
def roll(dices):
    list_dices = [dices[random.randrange(0, 4, 1)] for _ in range(3)]
    return list_dices


# Выбор костей игроком
def gamer_choice(list_dices):
    list_dices = list_dices
    list_name_dice = [dice.name for dice in list_dices]
    print('Ваши кости:', *list_name_dice)
    flag1, flag2 = False, False

    while flag1 is False:
        defense_dice = input('Выберете кость для защиты')
        if defense_dice in list_name_dice:
            flag1 = True
            list_name_dice.remove(defense_dice)
            print('У вас остались', *list_name_dice)
        else:
            print('Некорректный выбор')
    while flag2 is False:
        attack_dice = input('Выберете кость для нападения')
        if attack_dice in list_name_dice:
            flag2 = True
            list_name_dice.remove(attack_dice)

        else:
            print('Некорректный выбор')

    return attack_dice, defense_dice


# Выбор костей ботом
def bot_choice(list_dices):
    print('Вашему сопернику выпали:', *[dice.name for dice in list_dices])
    list_dices_bot = [list_dices[random.randrange(0, 3, 1)] for _ in range(3)]
    defense_dice_bot_fo_work = random.choice(list_dices_bot)
    defense_dice_bot = defense_dice_bot_fo_work.name
    list_dices_bot.remove(defense_dice_bot_fo_work)
    attack_dice_bot = random.choice(list_dices_bot).name
    return defense_dice_bot, attack_dice_bot


# Сравнение костей
def check_win():
    list_name_dices = [dice.name for dice in dices]

    defense_dice_bot, attack_dice_bot = bot_choice(roll(dices))
    attack_dice, defense_dice = gamer_choice(roll(dices))

    index_attack_dice_gamer = list_name_dices.index(attack_dice)
    index_defense_dice_gamer = list_name_dices.index(defense_dice)
    index_defense_dice_bot = list_name_dices.index(defense_dice_bot)
    index_attack_dice_bot = list_name_dices.index(attack_dice_bot)

    weakness_attack_dice_gamer = dices[index_attack_dice_gamer].weakness
    weakness_defense_dice_gamer = dices[index_defense_dice_gamer].weakness

    print(f'Соперник выбрал {attack_dice_bot} для нападения и {defense_dice_bot} для защиты')

    if attack_dice_bot in weakness_defense_dice_gamer:
        attack_bot = dices[index_attack_dice_bot].attack()
        defense_gamer = 0
    else:
        attack_bot = 0
        defense_gamer = dices[index_defense_dice_gamer].defense()
    if defense_dice_bot in weakness_defense_dice_gamer:
        attack_gamer = 0
        defense_bot = dices[index_defense_dice_bot].defense()
    else:
        attack_gamer = dices[index_attack_dice_gamer].attack()
        defense_bot = 0

    player_points = attack_gamer + defense_gamer
    bot_points = attack_bot + defense_bot

    return player_points, bot_points
