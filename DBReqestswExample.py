import sqlite3
from DBRequests import *


conn = sqlite3.connect('Databases/DB1.db')
cursor = conn.cursor()


print('Найти предметы определенной редкости')
ProductsOfRarity_ = ProductsOfRarity(cursor, 'Arcana')
for ID, Name, Rarity, Hero, Price in ProductsOfRarity_:  # Вывод
    print("{:2} {:30} {:9} {:20} {:6}".format(ID, Name, Rarity, Hero, Price))
print()


print('Найти предметы на определенного героя')
ProductsOfHero_ = ProductsOfHero(cursor, 'Pudge')
for ID, Name, Rarity, Hero, Price in ProductsOfHero_:  # Вывод
    print("{:2} {:30} {:9} {:20} {:6}".format(ID, Name, Rarity, Hero, Price))
print()


print('Найти предметы определенной редкости на определенного героя')
ProductsOfRarityAndHero_ = ProductsOfRarityAndHero(cursor, 'Teches', 'Arcana')
for ID, Name, Rarity, Hero, Price in ProductsOfRarityAndHero_:  # Вывод
    print("{:2} {:30} {:9} {:20} {:6}".format(ID, Name, Rarity, Hero, Price))
print()


print('Найти предметы в определенном ценовом диапазоне')
ProductsPriceBetween_ = ProductsPriceBetween(cursor, 1000, 1700)
for ID, Name, Rarity, Hero, Price in ProductsPriceBetween_:  # Вывод
    print("{:2} {:30} {:9} {:20} {:6}".format(ID, Name, Rarity, Hero, Price))
print()


print('Отсортировать предметы по редкости и стоимости')
ProductsSortedByRarityAndPrice_ = ProductsSortedByRarityAndPrice(cursor)
for ID, Name, Rarity, Hero, Price in ProductsSortedByRarityAndPrice_:  # Вывод
    print("{:2} {:30} {:9} {:20} {:6}".format(ID, Name, Rarity, Hero, Price))
print()


conn.close()