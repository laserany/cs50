from django.contrib import admin
from orders.models import RegularTopping, RegularPizza, SicilianTopping, SicilianPizza, Sub, Pasta, Salad, DinnerPlatter
# Register your models here.
admin.site.register(RegularTopping)
admin.site.register(RegularPizza)
admin.site.register(SicilianTopping)
admin.site.register(SicilianPizza)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(DinnerPlatter)
