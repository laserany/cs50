from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class RegularPizza(models.Model):
    size = models.CharField(max_length=2, choices=[('SM', 'Small'), ('LR', 'Large')], default='LR')
    number_of_toppings = models.CharField(max_length=1, choices=[('C', 'Cheese'), ('1', '1'), ('2', '2'), ('3', '3'), ('S', 'Special')], default='0')
    price = models.FloatField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    placed = models.BooleanField(default=False)
    def save(self):
        if not self.id:
            if self.size == 'SM':
                if self.number_of_toppings == 'C':
                    self.price = 12.70
                elif self.number_of_toppings == '1':
                    self.price = 13.70
                elif self.number_of_toppings == '2':
                    self.price = 15.20
                elif self.number_of_toppings == '3':
                    self.price = 16.20
                elif self.number_of_toppings == 'S':
                    self.price = 17.75
            elif self.size == 'LR':
                if self.number_of_toppings == 'C':
                    self.price = 17.95
                elif self.number_of_toppings == '1':
                    self.price = 19.95
                elif self.number_of_toppings == '2':
                    self.price = 21.95
                elif self.number_of_toppings == '3':
                    self.price = 23.95
                elif self.number_of_toppings == 'S':
                    self.price = 25.95
        super(RegularPizza, self).save()

class RegularTopping(models.Model):
    topping = models.CharField(max_length=30, choices=[('Pepperoni', 'Pepperoni'), ('Sausage', 'Sausage'), ('Mushrooms', 'Mushrooms'), ('Onions', 'Onions'), ('Ham', 'Ham'), ('Canadian Bacon', 'Canadian Bacon'), ('Pineapple', 'Pineapple'), ('Eggplant', 'Eggplant'), ('Tomato & Basil', 'Tomato & Basil'), ('Green Peppers', 'Green Peppers'), ('Hamburger', 'Hamburger'), ('Spinach', 'Spinach'), ('Artichoke', 'Artichoke'), ('Buffalo Chicken', 'Buffalo Chicken'), ('Barbecue Chicken', 'Barbecue Chicken'), ('Anchovies', 'Anchovies'), ('Black Olives', 'Black Olives'), ('Fresh Garlic', 'Fresh Garlic'), ('Zucchini', 'Zucchini')])
    regular = models.ForeignKey(RegularPizza, on_delete=models.CASCADE, null=True)

class SicilianPizza(models.Model):
    size = models.CharField(max_length=2, choices=[('SM', 'Small'), ('LR', 'Large')], default='LR')
    number_of_toppings = models.CharField(max_length=1, choices=[('C', 'Cheese'), ('1', '1'), ('2', '2'), ('3', '3'), ('S', 'Special')], default='0')
    price = models.FloatField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    placed = models.BooleanField(default=False)
    def save(self):
        if self.size == 'SM':
            if self.number_of_toppings == 'C':
                self.price = 24.45
            elif self.number_of_toppings == '1':
                self.price = 26.45
            elif self.number_of_toppings == '2':
                self.price = 28.45
            elif self.number_of_toppings == '3':
                self.price = 29.45
            elif self.number_of_toppings == 'S':
                self.price = 30.45
        elif self.size == 'LR':
            if self.number_of_toppings == 'C':
                self.price = 38.70
            elif self.number_of_toppings == '1':
                self.price = 40.70
            elif self.number_of_toppings == '2':
                self.price = 42.70
            elif self.number_of_toppings == '3':
                self.price = 44.70
            elif self.number_of_toppings == 'S':
                self.price = 45.70
        super(SicilianPizza, self).save()

class SicilianTopping(models.Model):
    topping = models.CharField(max_length=30, choices=[('Pepperoni', 'Pepperoni'), ('Sausage', 'Sausage'), ('Mushrooms', 'Mushrooms'), ('Onions', 'Onions'), ('Ham', 'Ham'), ('Canadian Bacon', 'Canadian Bacon'), ('Pineapple', 'Pineapple'), ('Eggplant', 'Eggplant'), ('Tomato & Basil', 'Tomato & Basil'), ('Green Peppers', 'Green Peppers'), ('Hamburger', 'Hamburger'), ('Spinach', 'Spinach'), ('Artichoke', 'Artichoke'), ('Buffalo Chicken', 'Buffalo Chicken'), ('Barbecue Chicken', 'Barbecue Chicken'), ('Anchovies', 'Anchovies'), ('Black Olives', 'Black Olives'), ('Fresh Garlic', 'Fresh Garlic'), ('Zucchini', 'Zucchini')])
    sicilian = models.ForeignKey(SicilianPizza, on_delete=models.CASCADE, null=True)

class Sub(models.Model):
    size = models.CharField(max_length=2, choices=[('SM', 'Small'), ('LR', 'Large')], default='LR')
    sub = models.CharField(max_length=30, choices=[('Cheese', 'Cheese'), ('Italian', 'Italian'), ('Ham + Cheese', 'Ham + Cheese'), ('Meatball', 'Meatball'), ('Tuna', 'Tuna'), ('Turkey', 'Turkey'), ('Chicken Parmigiana', 'Chicken Parmigiana'), ('Eggplant Parmigiana', 'Eggplant Parmigiana'), ('Steak', 'Steak'), ('Steak + Cheese', 'Steak + Cheese'), ('Sausage, Peppers & Onions', 'Sausage, Peppers & Onions'), ('Hamburger', 'Hamburger'), ('Cheeseburger', 'Cheeseburger'), ('Fried Chicken', 'Fried Chicken'), ('Veggie', 'Veggie')], default='Cheese')
    adds = models.CharField(max_length=30, choices=[('Mushrooms', 'Mushrooms'), ('Green Peppers', 'Green Peppers'), ('Onions', 'Onions'), ('Extra Cheese on any sub', 'Extra Cheese on any sub')])
    price = models.FloatField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    placed = models.BooleanField(default=False)
    def save(self):
        if self.size == 'SM':
            if self.sub in ['Cheese', 'Italian', 'Ham + Cheese', 'Meatball', 'Tuna', 'Eggplant Parmigiana', 'Steak']:
                self.price = 6.50
            elif self.sub in ['Turkey', 'Chicken Parmigiana']:
                self.price = 7.50
            elif self.sub in ['Steak + Cheese', 'Fried Chicken', 'Veggie']:
                self.price = 6.95
            elif self.sub == 'Hamburger':
                self.price = 4.60
            elif self.sub == 'Cheeseburger':
                self.price = 5.10
        elif self.size == 'LR':
            if self.sub in ['Cheese', 'Italian', 'Ham + Cheese', 'Meatball', 'Tuna', 'Eggplant Parmigiana', 'Steak']:
                self.price = 7.95
            elif self.sub in ['Turkey', 'Chicken Parmigiana', 'Steak + Cheese', 'Sausage, Peppers & Onions', 'Fried Chicken', 'Veggie']:
                self.price = 8.50
            elif self.sub == 'Hamburger':
                self.price = 6.95
            elif self.sub == 'Cheeseburger':
                self.price = 7.45
        if self.adds:
            self.price += 0.50
        super(Sub, self).save()

class Pasta(models.Model):
    pasta = models.CharField(max_length=30, choices=[('Baked Ziti w/Mozzarella', 'Baked Ziti w/Mozzarella'), ('Baked Ziti w/Meatballs', 'Baked Ziti w/Meatballs'), ('Baked Ziti w/Chicken', 'Baked Ziti w/Chicken')], default='Baked Ziti w/Mozzarella')
    price = models.FloatField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    placed = models.BooleanField(default=False)
    def save(self):
        if self.pasta == 'Baked Ziti w/Mozzarella':
            self.price = 6.50
        elif self.pasta == 'Baked Ziti w/Meatballs':
            self.price = 8.75
        elif self.pasta == 'Baked Ziti w/Chicken':
            self.price = 9.75
        super(Pasta, self).save()

class Salad(models.Model):
    salad = models.CharField(max_length=30, choices=[('Garden Salad', 'Garden Salad'), ('Greek Salad', 'Greek Salad'), ('Antipasto', 'Antipasto'), ('Salad w/Tuna', 'Salad w/Tuna')], default='Garden Salad')
    price = models.FloatField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    placed = models.BooleanField(default=False)
    def save(self):
        if self.salad == 'Garden Salad':
            self.price = 6.25
        elif self.salad in ['Greek Salad', 'Antipasto', 'Salad w/Tuna']:
            self.price = 8.25
        super(Salad, self).save()

class DinnerPlatter(models.Model):
    size = models.CharField(max_length=2, choices=[('SM', 'Small'), ('LR', 'Large')], default='LR')
    dinner_platter = models.CharField(max_length=30, choices=[('Garden Salad', 'Garden Salad'), ('Greek Salad', 'Greek Salad'), ('Antipasto', 'Antipasto'), ('Baked Ziti', 'Baked Ziti'), ('Meatball Parm', 'Meatball Parm'), ('Chicken Parm', 'Chicken Parm')], default='Garden Salad')
    price = models.FloatField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    placed = models.BooleanField(default=False)
    def save(self):
        if self.size == 'SM':
            if self.dinner_platter in ['Garden Salad', 'Baked Ziti']:
                self.price = 40.00
            elif self.dinner_platter in ['Greek Salad', 'Antipasto', 'Meatball Parm']:
                self.price = 50.00
            elif self.dinner_platter == 'Chicken Parm':
                self.price = 55.00
        elif self.size == 'LR':
            if self.dinner_platter in ['Garden Salad', 'Baked Ziti']:
                self.price = 65.00
            elif self.dinner_platter in ['Greek Salad', 'Antipasto', 'Meatball Parm']:
                self.price = 75.00
            elif self.dinner_platter == 'Chicken Parm':
                self.price = 85.00
        super(DinnerPlatter, self).save()