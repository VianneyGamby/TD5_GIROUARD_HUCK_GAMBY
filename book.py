import abc

class Book:
    def __init__(self, name):
        self.name = name   
        self.order = []

    def insert_buy(self, quantite, price):
        orderbuy = BuyOrder(quantite=quantite, price=price)
        self.order.append(orderbuy)
        print(f"--- Insert {orderbuy} id={len(self.order)} on {self.name}")
        print(f"Book on {self.name}")
        for i in range(len(self.order)):
            print(f"         {self.order[i]} id={i}")
        print(f"------------------------")

    def insert_sell(self, quantite, price):
        ordersell = SellOrder(quantite=quantite, price=price)
        self.order.append(ordersell)
        print(f"--- Insert {ordersell} id={len(self.order)} on {self.name}")
        print(f"Book on {self.name}")
        for i in range(len(self.order)):
            print(f"         {self.order[i]} id={i}")
        print(f"------------------------")

class Order(metaclass=abc.ABCMeta): 
    def __init__(self, quantite, price):
        self.quantite = quantite
        self.price = price
    
    def __str__(self) -> str:
        return f"{self.quantite}@{self.price}"

class BuyOrder(Order) :
    def __init__(self,quantite,price):
        self.type = "BUY"
        super().__init__(quantite,price)
    
    def __str__(self) -> str:
        return f"{self.type} {super().__str__()}"

class SellOrder(Order) :
    def __init__(self, quantite, price):
        self.type = "SELL"
        super().__init__(quantite,price)
        
    def __str__(self) -> str:
        return f"{self.type} {super().__str__()}"
 