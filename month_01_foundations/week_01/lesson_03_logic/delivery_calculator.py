# запрашиваем исходные данные. стоимость и город
price = float(input("Введите сумму заказа: "))
city = input("Введите город доставки: ")
print()

# условие расчета суммы доставки
if price > 3000:
    shipping_cost = 0
elif city.lower() == "москва":
    shipping_cost = 300
elif city.lower() == "санкт-петербург":
    shipping_cost = 400
else:
    shipping_cost = 500

# вывод общей стоимости
print(f"сумма заказа - {price} + доставка - {shipping_cost} = общая стоимость - {price + shipping_cost}")
