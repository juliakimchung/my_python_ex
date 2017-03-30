lottery_player = {
    'name': "Roy",
    'numbers': (13,25,44,66,71)
}

class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (13,25,44,66,71)

    def total(self):
        return sum(self.numbers)


player_one =LotteryPlayer("Roy")
player_two =LotteryPlayer("Joy")

print(player_two.name)
print(player_two.total())
print(player_one == player_two)


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

anna = Student("Anna", "MIT")
anna.marks.append(56)
anna.marks.append(64)
print(anna.average())
print(anna.marks)

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []
        # You'll need 'name' as an argument to this method.
        # Then, initialise 'self.name' to be the argument, and 'self.items' to be an empty list.
    
    def add_item(self, name, price):
        item = {"name":name, "price": price}
        self.items.append(item)
        return self.items
        # Create a dictionary with keys name and price, and append that to self.items.

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total
            
        # Add together all item prices in self.items and return the total.

store = Store("pottery barn")
print(store.add_item('tableset', 2200.00))
print(store.add_item('bedset', 1999.00))
print(store.add_item('drawerset', 3000.00))
print(store.items)
print(store.stock_price())



