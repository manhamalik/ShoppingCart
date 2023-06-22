from flask import Flask, render_template, request, redirect

app = Flask(__name__)

class List:
    def __init__(self):
        self.items = []

    def __str__(self):
        return str(self.items)

    def __len__(self):
        return len(self.items)

    def __contains__(self, item):
        return item in self.items

    def __getitem__(self, index):
        return self.items[index]

    def __setitem__(self, index, value):
        self.items[index] = value

    def insert(self, index, item):
        self.items = self.items[:index] + [item] + self.items[index:]

    def append(self, item):
        self.items.append(item)

    def remove(self, item):
        self.items = [x for x in self.items if x != item]

    def linear_search(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                return i
        return -1

    def index(self, item):
        return self.items.index(item)

    def find(self, item):
        for i in range(len(self.items)):
            if self.items[i] == item:
                return True
        return False

    def count(self, item):
        return self.items.count(item)

    def max(self):
        return max(self.items)

    def min(self):
        return min(self.items)


# Initialize the shopping cart as an instance of the List class
shopping_cart = List()

@app.route('/')
def index():
    food_items = [
        "Apples",
        "Eggs",
        "Almonds",
        "Spinach",
        "Avocados",
        "Sushi",
        "Strawberries",
        "Oranges",
        "Cauliflower",
        "Tomatoes",
        "Blueberries",
        "Bananas"
    ]
    return render_template('index.html', food_items=food_items, cart=shopping_cart)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    item_name = request.form['item_name']
    shopping_cart.append(item_name)
    return redirect('/')

@app.route('/remove_from_cart', methods=['POST'])
def remove_from_cart():
    item_name = request.form['item_name']
    shopping_cart.remove(item_name)
    return redirect('/')

app.run(host='0.0.0.0', port=81, debug=True)
