class Item(object):
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity


class Cart(object):
    def __init__(self):
        self.content = {}

    def add_item(self, item):
        if item.id not in self.content:
            self.content.update({item.id : item})
            return
        for item_id, item_detail in self.content.items():
            if item_id == item.id:
                self.content[item_id].quantity += item.quantity

    def remove_item(self, item_id):
        self.content.pop(item_id)

    def total_price(self):
        total = 0
        for item in self.content.values():
            total += item.price
        return total

    def empty(self):
        self.content.clear()

    def get_number_of_items(self):
        return sum([item.quantity for item in self.content.values()])

if __name__ == '__main__':
    item1 = Item(1, "Banana", 1., 1)
    item2 = Item(2, "Eggs", 1., 2)
    item3 = Item(3, "Donut", 1., 5)
    cart = Cart()
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    print("You have %i items in your cart for a total of $%.02f" % (cart.get_number_of_items(), cart.total_price()))
    cart.remove_item(1)
    print("You have %i items in your cart for a total of $%.02f" % (cart.get_number_of_items(), cart.total_price()))
