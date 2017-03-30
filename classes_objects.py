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

    @staticmethod # all object share the same method, no need for a decorator which is self
    def go_to_school():
        print("I'm going to school")
    @classmethod 
    def go_to_school(cls):
        print("I'm going to school")
        # print("I'm going to {}".format(self.school))

anna = Student("Anna", "MIT")
rolf = Student("Rolf", "Oxford")
rolf.go_to_school()
anna.marks.append(56)
anna.marks.append(64)
anna.go_to_school()
Student.go_to_school()
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
        print (total)
            
        # Add together all item prices in self.items and return the total.


    @classmethod
    def franchise(cls, store):
        print (store.name)

    @staticmethod
    def store_detail(store):
        print (store.stock_price)

store = Store("Test")
store2 = Store("Amazon")
store.add_item('tableset', 2200.00)
store.add_item('bedset', 1999.00)
store.add_item('drawerset', 3000.00)
store2.add_item('keyboard', 1600.00)
print(store.items)
store.stock_price()
Store.franchise(store)
Store.franchise(store2)
Store.stock_price(store2)
Store.stock_price(store)



