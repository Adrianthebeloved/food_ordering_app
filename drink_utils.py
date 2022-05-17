from fruit_utils import Fruitmenu

class Drink(Fruitmenu):
    def __init__(self,name,price, volume):
        # self.name = name
        # self.price = price
        super().__init__(name,price)
        self.volume = volume
        
    def info(self):
        return self.name +': $' + str(self.price) + ' (' + str(self.volume) + 'mL)'
        