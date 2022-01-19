from datetime import datetime
from enum import unique
from os import name
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import backref

# Перед запуском убедитесь, что файл (TestCopyDB1_1.db) отсутствует в директории (testing)

app = Flask(__name__) # объект приложения Flask
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///TestCopyDB1_1.db' # привязываем базу данных
db = SQLAlchemy(app) # создаем объект SQLAlchemy


class rarity(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    rarity_name = db.Column(db.String, unique = True)
    rarity_color = db.Column(db.String)

    def __repr__(self):
        return f'{self.id} {self.rarity_name}'

class hero(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    hero_name = db.Column(db.String, unique = True)
    hero_ico = db.Column(db.String)
    
    def __repr__(self):
        return f'{self.id} {self.hero_name}'

class products(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True)
    rarity_id = db.Column(db.Integer, db.ForeignKey('rarity.id'))
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'))
    count = db.Column(db.Integer)
    price = db.Column(db.Integer)

    rarity = db.relationship('rarity', backref = db.backref('products', lazy = False))
    hero = db.relationship('hero', backref = db.backref('products', lazy = False))

    def __repr__(self):
        return f'{self.id} {self.name}'

class users(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String, unique = True, nullable = False)
    mail = db.Column(db.String, unique = True, nullable = False)
    password = db.Column(db.String, nullable = False)

    def __repr__(self):
        return f'{self.id} {self.name} {self.mail}'

class deals(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    date = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'))

    users = db.relationship('users', backref = db.backref('deals', lazy = False))
    products = db.relationship('products', backref = db.backref('deals', lazy = False))

    def __repr__(self):
        return f'{self.id} {self.date} {self.user_id} {self.product_id}'


db.create_all()

db.session.add(rarity(rarity_name = 'Common', rarity_color = '#b0c3d9'))
db.session.add(rarity(rarity_name = 'Uncommon', rarity_color = '#5e98d9'))
db.session.add(rarity(rarity_name = 'Rare', rarity_color = '#4b69ff'))
db.session.add(rarity(rarity_name = 'Mythical', rarity_color = '#8847ff'))
db.session.add(rarity(rarity_name = 'Legendary', rarity_color = '#d32ce6'))
db.session.add(rarity(rarity_name = 'Immortal', rarity_color = '#b28a33'))
db.session.add(rarity(rarity_name = 'Arcana', rarity_color = '#ade55c'))
db.session.add(rarity(rarity_name = 'Ancient', rarity_color = '#eb4b4b'))

db.session.add(hero(hero_name = 'Pudge'))
db.session.add(hero(hero_name = 'Shadow Fiend'))
db.session.add(hero(hero_name = 'Teches'))

db.session.add(products(name = 'Feast of Abscession', rarity_id = 7, hero_id = 1, count = 3, price = 1799))
db.session.add(products(name = 'Demon Eater', rarity_id = 7, hero_id = 2, count = 2, price = 1699))
db.session.add(products(name = 'Swine of the Sunken Galley', rarity_id = 7, hero_id = 3, count = 1, price = 1599))

db.session.add(users(name = 'Alexandr', mail = 'mail@mail.com', password = '1234567890'))

db.session.add(deals(date = datetime.now(), user_id =  1, product_id = 2))

db.session.commit()

print(*rarity.query.all(), sep = '\n', end = '\n---\n')
print(*hero.query.all(), sep = '\n', end = '\n---\n')
print(*products.query.all(), sep = '\n', end = '\n---\n')
print(*users.query.all(), sep = '\n', end = '\n---\n')
print(*deals.query.all(), sep = '\n', end = '\n---\n')