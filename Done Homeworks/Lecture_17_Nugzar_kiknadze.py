

class car:
    def __init__(self, model , year, price=0):
        assert type(model) is str , 'Enter string in model field'
        assert year > 2010 , 'Only cars from 2011 are welcome'
        assert price >= 0 , 'Price cant be negative'
        
        self.__model = model
        self.year = year
        self.price = price


    @property
    def model(self):
        print("cant change me! ")
    
    @model.setter
    def model(self,value):
        assert type(value) is str , 'Enter string in model field'    


car1 = car("BMW X6",2020)

car1._model = "BmW X5"

print(car1.price)
