# Я буду описывать настольную игру Манчкин

class Player:

    def __init__(self):
        self. lvl = 1  # Уровень игрока (максимум 10)
        self.bonus = 0  # Чтобы получить бонус, нужно надеть снаряжение
        self.power = self.lvl + self.bonus  # Сила игрока - это уровень + его суммарные бонусы
        self.items = []  # Снаряжение игрока
        self.gold = 1000  # Золото игрока (валюта)
        self.type = 'human'  # Класс игрока, изначально все люди, но могут поменять его на эльфа, воина или вора

    # Игрок может драться с монстрами, он побеждает, если его сила больше силы монстра

    def battle(self, monster):
        if self.power > monster.power:
            self.lvl += 1  # За победу дается один уровень и какое-то кол-во золота
            self.gold += monster.prize
            print('You won')
        else:
            print('You die')  # Если игрок проигрывает, он умирает
        self.power = self.lvl + self.bonus

    def buy_lvl(self, number):  # Игрок может покупать доп. уровни за золото
        if self.gold >= 1000 * number:
            self.lvl += 1 * number
            self.gold -= 1000 * number
        else:
            print('Not enough gold')

# Каждый игрок выбирает себе класс, кем он хочет быть: ельфом, вором или воином.
# При желании, он может остаться человеком


class Elf(Player):
    """Если ты стал эльфом, то можешь убежать от любого противника,
    если не можешь его одолеть"""
    type = 'elf'

    def escape(self):
        print('I ran away')


class Warrior(Player):
    """При равенстве сил, воин побеждает (в драках)"""
    type = 'warrior'

    def morale(self, monster):
        monster.power -= 1


class Thief(Player):
    """Когда вор дерется с монстром, он может украсть его силу (максимум 3) """
    type = 'thief'

    def theft(self, monster, number):
        if number <= 3:
            monster.power -= number
            self.power += number

# Также в игре существуют монстры разных уровней. Игрокам надо их побеждать, чтобы получать...
# ...за них золото и уровни


class Monster:
    def __init__(self, power, prize):
        self.power = power
        self.prize = prize


player_1 = Warrior()  # Создадим первого игрока, пусть он будет воином
# print(player_1.type)
goblin = Monster(1, 300)  # Создамим монстра, пусть он будет гоблином, с силой 1 и с 300-ми голдами

# Предположим игрок 1 решил напасть на гоблина
# Как воин, он может использовать сораль и победить при равенстве сил
player_1.morale(goblin)
player_1.battle(goblin)

# Игрок 1 выиграл и получил за монстра один уровень и 300 голдов
print(player_1.lvl)
print(player_1.gold)

# Создадим друго монстра, пусть он будет лепреконом, с силой один 2 и с 700-ми голдами
leprechaun = Monster(2, 700)

# Игрок 1 опять решил напасть. Он также использует свою мораль, т.к. у них одинаковая сила
player_1.morale(leprechaun)
player_1.battle(leprechaun)

# Игрок 1 опять выиграл и получил за монстра один уровень и 700 голдов
print(player_1.lvl)
print(player_1.gold)

# Тперь у него 2000 голдов, и он может купить себе два уровня
player_1.buy_lvl(2)
print(player_1.lvl)

# В игре побеждает тот игрок, кто первым достигнет 10-го уровня
