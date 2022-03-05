import copy

cars = [
    {
        'brand': 'Dacia',
        'model': 'Logan',
        'hp' : 75,
        'price': 900
    },
    {
        'brand': 'Seat',
        'model': 'Leon',
        'hp' : 130,
        'price': 3000
    },
    {
        'brand' : 'Ferrari',
        'model' : 'Rocher',
        'hp' : 230,
        'price' : 7000
    }
]

def slow_car(car):
    slow_cars = copy.deepcopy(car)
    slow_cars["hp_smaller_than_120"] = True if slow_cars['hp'] < 120 else False
    return slow_cars

slow_cars = map(slow_car, cars)
print('slow_cars =', list(slow_cars))

def fast_car(car):
    fast_cars = copy.deepcopy(car)
    fast_cars["hp >=_120_<_180"] = True if fast_cars['hp'] >= 120 < 180 else False
    return fast_cars

fast_cars = map(fast_car, cars)
print('fast_cars =', list(fast_cars))

def sport_car(car):
    sport_cars = copy.deepcopy(car)
    sport_cars["hp > 180"] = True if sport_cars['hp'] > 180 else False
    return sport_cars

sport_cars = map(sport_car, cars)
print('sport_cars =', list(sport_cars))

def cheap_car(car):
    cheap_cars = copy.deepcopy(car)
    cheap_cars["price < 1000"] = True if cheap_cars['price'] < 1000 else False
    return cheap_cars

cheap_cars = map(cheap_car, cars)
print('cheap_cars =', list(cheap_cars))

def medium_car(car):
    medium_cars = copy.deepcopy(car)
    medium_cars["price >= 1000 < 5000"] = True if medium_cars['price'] >= 1000 < 5000 else False
    return medium_cars

medium_cars = map(medium_car, cars)
print('medium_cars =', list(medium_cars))

def expensive_car(car):
    expensive_cars = copy.deepcopy(car)
    expensive_cars["price > 5000"] = True if medium_cars['price'] > 5000 else False
    return expensive_cars

expensive_cars = map(medium_car, cars)
print('expensive_cars =', list(expensive_cars))



with open ('input.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    for new_car in cars:
        csv_writer.writerow(new_car)

with open('slow_car.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',')

    for slow_car in cars:
        csv_writer.writerow(slow_car)

# import os
#
# for dir_entry in os.scandir():
#     if os.path.isfile(dir_entry):
#         print(f'{dir_entry.name} is file.')
#     else:
#         print(f'{dir_entry.name} is directory')
