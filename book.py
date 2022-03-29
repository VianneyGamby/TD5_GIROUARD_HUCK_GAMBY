
from distutils.util import execute

class Book:
    def __init__(self, name):
        self.name = name   
        self.order = [] 
        self.executed = [] 

    
    def executeorder(self,typeorder):
        tab = []
        q = self.order[len(self.order)-1].quantite
        for i in range(len(self.order)-2):
            text = self.order[i].__str__()
            if q >0 :
                if typeorder not in text and self.order[i].price == self.order[len(self.order)-1].price:
                    if self.order[i].quantite < self.order[len(self.order)-1].quantite : 
                        self.order[len(self.order)-1].quantite -= self.order[i].quantite
                        q -= self.order[i].quantite
                        self.executed.append(f"Executed {self.order[i].quantite}@{self.order[i].price}")
                        tab.append(self.order[i])
                    elif self.order[i].quantite > self.order[len(self.order)-1].quantite :
                        self.order[i].quantite -= self.order[len(self.order)-1].quantite
                        self.executed.append(f"Executed {self.order[len(self.order)-1].quantite}@{self.order[len(self.order)-1].price}")
                        tab.append(self.order[len(self.order)-1])
                    else : 
                        self.executed.append(f"Executed {self.order[i].quantite}@{self.order[i].price}")
                        tab.append(self.order[i])
                        tab.append(self.order[len(self.order)-1])
                        q = 0   
        for i in tab :
            for j in range(len(self.order)-1):
                if i.__str__() == self.order[j].__str__() :
                    del self.order[j]

    def insert_buy(self, quantite, price):
        orderbuy = BuyOrder(quantite=quantite, price=price)
        self.order.append(orderbuy)
        print(f"--- Insert {orderbuy} id={len(self.order)} on {self.name}")
        print(f"Book on {self.name}")
        typeorder = "BUY"
        self.executeorder(typeorder)
        for i in range(len(self.executed)):
            print(self.executed[i])
        for i in range(len(self.order)):
            print(f"         {self.order[i]} id={i}")
        print(f"------------------------")

    def insert_sell(self, quantite, price):
        ordersell = SellOrder(quantite=quantite, price=price)
        self.order.append(ordersell)
        print(f"--- Insert {ordersell} id={len(self.order)} on {self.name}")
        print(f"Book on {self.name}")
        typeorder = "SELL"
        self.executeorder(typeorder)
        for i in range(len(self.executed)):
            print(self.executed[i])
        for i in range(len(self.order)):
            print(f"         {self.order[i]} id={i}")
        print(f"------------------------")
      
class Order(): 
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
 