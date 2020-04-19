from django.http import HttpResponse
from django.shortcuts import render, redirect
from orders.forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from orders.models import *
from django.core.mail import send_mail
import sys

# Create your views here.
@login_required
def index(request):
    context = {}
    added_to_cart = False
    cart_count = len(RegularPizza.objects.filter(user=request.user, placed=False)) + len(SicilianPizza.objects.filter(user=request.user, placed=False)) + len(Sub.objects.filter(user=request.user, placed=False)) + len(Pasta.objects.filter(user=request.user, placed=False)) + len(Salad.objects.filter(user=request.user, placed=False)) + len(DinnerPlatter.objects.filter(user=request.user, placed=False))
    context['cart_count'] = cart_count
    if request.method == 'GET':
        return render(request, 'index.html', context)
    elif request.method == 'POST':
        if 'selected-regular-pizza-type-order' in request.POST:
            regular_pizza = RegularPizza(size=request.POST['selected-regular-pizza-size-order'], number_of_toppings=request.POST['selected-regular-pizza-type-order'], user=request.user)
            regular_pizza.save()
            if 'selected-regular-pizza-topping-1-order' in request.POST:
                regular_topping = RegularTopping(topping=request.POST['selected-regular-pizza-topping-1-order'], regular=regular_pizza)
                regular_topping.save()
            if 'selected-regular-pizza-topping-2-order' in request.POST:
                regular_topping = RegularTopping(topping=request.POST['selected-regular-pizza-topping-2-order'], regular=regular_pizza)
                regular_topping.save()
            if 'selected-regular-pizza-topping-3-order' in request.POST:
                regular_topping = RegularTopping(topping=request.POST['selected-regular-pizza-topping-3-order'], regular=regular_pizza)
                regular_topping.save()
        elif 'selected-sicilian-pizza-type-order' in request.POST:
            sicilian_pizza = SicilianPizza(size=request.POST['selected-sicilian-pizza-size-order'], number_of_toppings=request.POST['selected-sicilian-pizza-type-order'], user=request.user)
            sicilian_pizza.save()
            if 'selected-sicilian-pizza-topping-1-order' in request.POST:
                sicilian_topping = SicilianTopping(topping=request.POST['selected-sicilian-pizza-topping-1-order'], sicilian=sicilian_pizza)
                sicilian_topping.save()
            if 'selected-sicilian-pizza-topping-2-order' in request.POST:
                sicilian_topping = SicilianTopping(topping=request.POST['selected-sicilian-pizza-topping-2-order'], sicilian=sicilian_pizza)
                sicilian_topping.save()
            if 'selected-sicilian-pizza-topping-3-order' in request.POST:
                sicilian_topping = SicilianTopping(topping=request.POST['selected-sicilian-pizza-topping-3-order'], sicilian=sicilian_pizza)
                sicilian_topping.save()
        elif 'selected-subs-type-order' in request.POST:
            if 'None' in request.POST['selected-subs-adds-order']:
                sub = Sub(size=request.POST['selected-subs-size-order'], sub=request.POST['selected-subs-type-order'], user=request.user)
                sub.save()
            else:
                sub = Sub(size=request.POST['selected-subs-size-order'], sub=request.POST['selected-subs-type-order'], adds=request.POST['selected-subs-adds-order'], user=request.user)
                sub.save()
        elif 'selected-pasta-type-order' in request.POST:
            pasta = Pasta(pasta=request.POST['selected-pasta-type-order'], user=request.user)
            pasta.save()
        elif 'selected-salad-type-order' in request.POST:
            salad = Salad(salad=request.POST['selected-salad-type-order'], user=request.user)
            salad.save()
        elif 'selected-dinner-platters-type-order' in request.POST:
            dinner_platter = DinnerPlatter(size=request.POST['selected-dinner-platters-size-order'],dinner_platter=request.POST['selected-dinner-platters-type-order'], user=request.user)
            dinner_platter.save()
        context['cart_count'] += 1
        context['added_to_cart'] = True
        return render(request, 'index.html', context)

@login_required        
def cart(request):
    regular_pizzas = request.user.regularpizza_set.filter(placed=False)
    sicilian_pizzas = request.user.sicilianpizza_set.filter(placed=False)
    subs = request.user.sub_set.filter(placed=False)
    pastas = request.user.pasta_set.filter(placed=False)
    salads = request.user.salad_set.filter(placed=False)
    dinner_platters = request.user.dinnerplatter_set.filter(placed=False)
    total_price = sum(regular_pizza.price for regular_pizza in regular_pizzas) + sum(sicilian_pizza.price for sicilian_pizza in sicilian_pizzas) + sum(sub.price for sub in subs) + sum(pasta.price for pasta in pastas) + sum(salad.price for salad in salads) + sum(dinner_platter.price for dinner_platter in dinner_platters)

    return render(request, 'cart.html', {'regular_pizzas': regular_pizzas,'sicilian_pizzas': sicilian_pizzas,'subs': subs,'pastas': pastas,'salads': salads,'dinner_platters': dinner_platters, 'total_price': total_price})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        form.save()
        return redirect('index')
    else:
        return render(request, 'registration/register.html', {'form': RegisterForm()})

@login_required
def place_order(request):
    regular_pizzas = request.user.regularpizza_set.filter(placed=False)
    for regular_pizza in regular_pizzas:
        regular_pizza.placed=True
        regular_pizza.save()
    sicilian_pizzas = request.user.sicilianpizza_set.filter(placed=False)
    for sicilian_pizza in sicilian_pizzas:
        sicilian_pizza.placed=True
        sicilian_pizza.save()
    subs = request.user.sub_set.filter(placed=False)
    for sub in subs:
        sub.placed=True
        sub.save()
    pastas = request.user.pasta_set.filter(placed=False)
    for pasta in pastas:
        pasta.placed=True
        pasta.save()
    salads = request.user.salad_set.filter(placed=False)
    for salad in salads:
        salad.placed=True
        salad.save()
    dinner_platters = request.user.dinnerplatter_set.filter(placed=False)
    for dinner_platter in dinner_platters:
        dinner_platter.placed=True
        dinner_platter.save()
    send_mail(
        'Pinnochio’s Pizza & Subs',
        'This is a confirmation email that your order has been placed!',
        'dotachessfan@outlook.com',
        [request.user.email],
        fail_silently=False,
        )
    return HttpResponse("You will receive a confirmation email shortly!")

@staff_member_required
def view_orders(request):
    regular_pizzas = RegularPizza.objects.filter(placed=True)
    sicilian_pizzas = SicilianPizza.objects.filter(placed=True)
    subs = Sub.objects.filter(placed=True)
    pastas = Pasta.objects.filter(placed=True)
    salads = Salad.objects.filter(placed=True)
    dinner_platters = DinnerPlatter.objects.filter(placed=True)
    return render(request, 'view_orders.html', {'regular_pizzas': regular_pizzas, 'sicilian_pizzas': sicilian_pizzas, 'subs': subs, 'pastas': pastas, 'salads': salads, 'dinner_platters': dinner_platters})