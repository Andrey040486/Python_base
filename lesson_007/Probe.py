# -*- coding: utf-8 -*-

from random import randint

from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 150
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def shopping_by_cat(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой для кота'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.cats_food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def get_a_cat(self):
        cprint('{} притащил кота'.format(self.name), color='cyan')
        self.fullness -= 10

    def go_to_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} Вьехал в дом'.format(self.name), color='cyan')

    def cleaning(self):
        cprint('{} убрал квартиру'.format(self.name), color='magenta')
        self.fullness -= 20
        self.house.dust -= 100

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 30:
            self.eat()
        elif self.house.food < 30:
            self.shopping()
        elif self.house.cats_food < 10:
            self.shopping_by_cat()
        elif self.house.dust > 100:
            self.cleaning()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def sleep(self):
        cprint('{} дрыхнет'.format(self.name), color='magenta')
        self.fullness -= 10

    def eat(self):
        cprint('{} ест'.format(self.name), color='magenta')
        self.fullness += 20
        self.house.cats_food -= 10

    def tears_wallpaper(self):
        cprint('{} дерет обои'.format(self.name), color='magenta')
        self.fullness -= 10
        self.house.dust += 5

    def __str__(self):
        return 'Я - {}, сытость {}'.format(
            self.name, self.fullness)

    def go_to_the_house(self, house):
        self.house = house

    def act(self):
        if self.fullness <= 0:
            cprint('{} сдох...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.tears_wallpaper()
        else:
            self.sleep()


class House:

    def __init__(self):
        self.food = 50
        self.money = 50
        self.cats_food = 0
        self.dust = 0

    def __str__(self):
        return 'В доме еды осталось {}, еды для кота осталось {}, денег осталось {}, загрязненность дома {}'.format(
            self.food, self.cats_food, self.money, self.dust)


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]
kisa = Cat(name='Тимошка')
my_sweet_home = House()
for citisen in citizens:
    citisen.go_to_the_house(house=my_sweet_home)
Man(name='Бивис').get_a_cat()
kisa.go_to_the_house(house=my_sweet_home)
for day in range(1, 366):
    print('================ день {} =================='.format(day))
    for citisen in citizens:
        citisen.act()
    kisa.act()
    print('--- в конце дня ---')
    for citisen in citizens:
        print(citisen)
    print(kisa)
    print(my_sweet_home)
