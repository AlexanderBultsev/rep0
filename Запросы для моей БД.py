import sqlite3


# Найти предметы определенной редкости
def ProductsOfRarity(cursor, RarityName: str):
    cursor.execute(f" \
        SELECT \
            ID, \
            Name, \
            (SELECT Rarity_name FROM Rarity WHERE ID = Rarity_ID), \
            (SELECT Hero_name FROM Hero WHERE ID = Hero_ID), \
            Price \
        FROM Products \
        WHERE Rarity_ID = (SELECT ID FROM Rarity WHERE Rarity_name = '{RarityName}');\
        ")
    return cursor.fetchall()


# Найти предметы на определенного героя
def ProductsOfHero(cursor, HeroName: str):
    cursor.execute(f" \
        SELECT \
            ID, \
            Name, \
            (SELECT Rarity_name FROM Rarity WHERE ID = Rarity_ID), \
            (SELECT Hero_name FROM Hero WHERE ID = Hero_ID), \
            Price \
        FROM Products \
        WHERE Hero_ID = (SELECT ID FROM Hero WHERE Hero_name = '{HeroName}');\
        ")
    return cursor.fetchall()


# Найти предметы определенной редкости на определенного героя
def ProductsOfRarityAndHero(cursor, HeroName: str, RarityName: str):
    cursor.execute(f" \
        SELECT \
            ID, \
            Name, \
            (SELECT Rarity_name FROM Rarity WHERE ID = Rarity_ID), \
            (SELECT Hero_name FROM Hero WHERE ID = Hero_ID), \
            Price \
        FROM Products \
        WHERE \
            Hero_ID = (SELECT ID FROM Hero WHERE Hero_name = '{HeroName}') \
            AND Rarity_ID = (SELECT ID FROM Rarity WHERE Rarity_name = '{RarityName}'); \
        ")
    return cursor.fetchall()


# Найти предметы в определенном ценовом диапазоне
def ProductsPriceBetween(cursor, MinPrice: int, MaxPrice: int):
    cursor.execute(f" \
        SELECT \
            ID, \
            Name, \
            (SELECT Rarity_name FROM Rarity WHERE ID = Rarity_ID), \
            (SELECT Hero_name FROM Hero WHERE ID = Hero_ID), \
            Price \
        FROM Products \
        WHERE Price BETWEEN {MinPrice} AND {MaxPrice}; \
        ")
    return cursor.fetchall()


# Отсортировать предметы по редкости и стоимости
def ProductsSortedByRarityAndPrice(cursor):
    cursor.execute(f" \
        SELECT \
            ID, \
            Name, \
            (SELECT Rarity_name FROM Rarity WHERE ID = Rarity_ID), \
            (SELECT Hero_name FROM Hero WHERE ID = Hero_ID), \
            Price \
        FROM Products \
        ORDER BY Rarity_ID DESC, Price ASC; \
        ")
    return cursor.fetchall()


conn = sqlite3.connect('Databases/DB1.db')
cursor = conn.cursor()


print('Найти предметы определенной редкости')
ProductsOfRarity_ = ProductsOfRarity(cursor, 'Arcana')

for ID, Name, Rarity, Hero, Price in ProductsOfRarity_:  # Вывод
    print(ID, Name, Rarity, Hero, Price)
print()


print('Найти предметы на определенного героя')
ProductsOfHero_ = ProductsOfHero(cursor, 'Pudge')

for ID, Name, Rarity, Hero, Price in ProductsOfHero_:  # Вывод
    print(ID, Name, Rarity, Hero, Price)
print()


print('Найти предметы определенной редкости на определенного героя')
ProductsOfRarityAndHero_ = ProductsOfRarityAndHero(cursor, 'Teches', 'Arcana')

for ID, Name, Rarity, Hero, Price in ProductsOfRarityAndHero_:  # Вывод
    print(ID, Name, Rarity, Hero, Price)
print()


print('Найти предметы в определенном ценовом диапазоне')
ProductsPriceBetween_ = ProductsPriceBetween(cursor, 1000, 1700)

for ID, Name, Rarity, Hero, Price in ProductsPriceBetween_:  # Вывод
    print(ID, Name, Rarity, Hero, Price)
print()


print('Отсортировать предметы по редкости и стоимости')
ProductsSortedByRarityAndPrice_ = ProductsSortedByRarityAndPrice(cursor)

for ID, Name, Rarity, Hero, Price in ProductsSortedByRarityAndPrice_:  # Вывод
    print(ID, Name, Rarity, Hero, Price)
print()

conn.close()