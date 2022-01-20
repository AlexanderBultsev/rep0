from flask import Flask, render_template, escape, abort

app = Flask(__name__)

class Item:
    def __init__(self, name = 'name', descr = 'description', price = 0, image = 'Logo.img', link = 'catalog.html'):
        self.name = name
        self.descr = descr
        self.price = price
        self.image = image
        self.link = link

ITEMS = [Item('Feast of Abscession', 'Аркана на Pudge', 1799, 'FeastofAbscession01.jpg', 'FeastofAbscession.html'), \
    Item('Demon Eater', 'Аркана на Shadow Fiend', 1699, 'DemonEater01.jpg', ''), \
    Item('Swine of the Sunken Galley', 'Аркана на Teches', 1599, 'SwineoftheSunkenGalley01.jpg', '')]

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/catalog')
def catalog():
    return render_template('catalog.html', items=ITEMS)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/product/<item>')
def show_item_profile(item):
    item = escape(item)
    for thing in ITEMS:
        if thing.name == item:
            return render_template('product.html', item=thing)
    return abort(404, description="not found")

if __name__ == '__main__':
    app.run(debug=True)