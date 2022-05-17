from fruit_utils import Fruitmenu

class Food(Fruitmenu):
    def __init__(self,name,price,calories):
        # self.name = name
        # self.price = price
        super().__init__(name,price)
        self.calories = calories
        
    def info(self):
        return self.name +': $' + str(self.price) + ' (' + str(self.calories) + 'kcal)'

    def calories(self):
        print('kcal:' + str(self.calories))

