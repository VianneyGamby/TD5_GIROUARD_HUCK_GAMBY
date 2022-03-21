class Book:

    def __init__(self, name):
        self.name = name   
        self.order = []

    def insert_buy(self,quantite,price):
        orderbuy = BuyOrder(quantite,price)
        self.order.append(orderbuy)

    def insert_sell(self,quantite,price):
        ordersell = SellOrder(quantite,price)
        self.order.append(ordersell)
class Order : 

    def __init__(self, quantite, price):
        self.quantite = quantite   
        self.price = price

class BuyOrder(Order) :
    def __init__(self):
        super().__init__(self)

class SellOrder(Order) :
    def __init__(self,quantite,price):
        super().__init__(self)