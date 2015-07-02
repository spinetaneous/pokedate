init -1 python:
    
    class Item:
        def __init__(self, name, cost):
            self.name = name
            self.cost = cost
    
    class Inventory:
        def __init__(self, money):
            self.money = money
            self.items = []
            
        def buy(self, item):
            if self.money >= item.cost:
                self.money -= item.cost
                self.items.append(item)
                return True
            else:
                return False
                
        def give(self, item):
            if item in self.items:
                self.items.remove(item)
                return True
            else:
                return False

        def has_item(self, item):
            if item in self.items:
                return True
            else:
                return False
        
        def earn(self, amount):
            self.money += amount