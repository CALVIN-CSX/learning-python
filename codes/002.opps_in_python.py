class Car:
    def __init__(self,model,year,color,for_sale):
        #self is basically similar  to this. from java
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
    def describe(self):
        print(f"{self.model} {self.year} {self.color} {self.for_sale}")
car1=Car('Ford',2024,"blue",False)
print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)
car1.describe()
