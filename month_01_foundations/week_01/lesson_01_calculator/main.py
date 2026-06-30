# Это мой первый скрипт. Он считает, сколько дней я прожил.

age = 25
days_in_year = 365
hours_in_a_day = 24
minutes_in_an_hour = 60
weeks_a_year = 52

days_lived = age * days_in_year
hours_lived = age * days_in_year * hours_in_a_day
minutes_lived = age * days_in_year * hours_in_a_day * minutes_in_an_hour
weeks_lived = age * weeks_a_year

print("Прожито недель: ", weeks_lived)
print("Прожито дней: ", days_lived)
print("Прожито часов: ", hours_lived)
print("Прожито минут: ", minutes_lived)