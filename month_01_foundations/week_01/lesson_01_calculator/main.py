# Это мой первый скрипт. Он считает, сколько дней я прожил.

age = 25
days_per_year = 365
hours_per_day = 24
minutes_per_hour = 60
weeks_per_year = 52

days_lived = age * days_per_year
hours_lived = days_lived * hours_per_day
minutes_lived = hours_lived * minutes_per_hour
weeks_lived = age * weeks_per_year

print("Прожито недель: ", weeks_lived)
print("Прожито дней: ", days_lived)
print("Прожито часов: ", hours_lived)
print("Прожито минут: ", minutes_lived)