showroom = set()

showroom.add("lamborghini")
showroom.add("tesla")
showroom.add("lexus")
showroom.add("acura")

print(len(showroom))

print("")

showroom.add("lamborghini")

print(showroom)

print("")

showroom.discard("lexus")

junkyard = {"tesla", "ford", "acura", "toyota", "honda"}

print(showroom.intersection(junkyard))

print("")

myShowroom = showroom.union(junkyard)

print(myShowroom)

print("")

myShowroom.discard("ford")
myShowroom.discard("toyota")

print(myShowroom)

print("")

makes = (
  (1, "Toyota"), (2, "Nissan"),
  (3, "Ford"), (4, "Mini"),
  (5, "Honda"), (6, "Dodge"),
)

models = (
  (1, "Altima", 2), (2, "Thunderbird", 3),
  (3, "Dart", 6), (4, "Accord", 5),
  (5, "Prius", 1), (6, "Countryman", 4),
  (7, "Camry", 1), (8, "F150", 3),
  (9, "Civic", 5), (10, "Ram", 6),
  (11, "Cooper", 4), (12, "Pilot", 5),
  (13, "Xterra", 2), (14, "Sentra", 2),
  (15, "Charger", 6)
)

colors = (
  (1, "Black" ), (2, "Charcoal" ), (3, "Red" ), (4, "Brick" ),
  (5, "Blue" ), (6, "Navy" ), (7, "White" ), (8, "Ivory" )
)

available_car_colors = (
  (1, 1), (1, 2), (1, 7),
  (2, 1), (2, 3), (2, 7),
  (3, 2), (3, 3), (3, 7),
  (4, 3), (4, 5), (4, 8),
  (5, 2), (5, 4), (5, 8),
  (6, 2), (6, 6), (6, 7),
  (7, 1), (7, 3), (7, 7),
  (8, 1), (8, 5), (8, 8),
  (9, 1), (9, 6), (9, 7),
  (10, 2), (10, 5), (10, 7),
  (11, 3), (11, 6), (11, 8),
  (12, 1), (12, 4), (12, 7),
  (13, 2), (13, 6), (13, 8),
  (14, 2), (14, 5), (14, 8),
  (15, 1), (15, 4), (15, 7)
)

available_cars = dict()

for makeTuple in makes:
        available_cars[makeTuple[1]] = available_models = dict()     
        for modelTuple in models:
            if modelTuple[2] == makeTuple[0]:
                available_models[modelTuple[1]] = colors_list = list()
                for colorJoinTuple in available_car_colors:
                    if colorJoinTuple[0] == modelTuple[0]:
                        colors_list.append(colors[colorJoinTuple[1] - 1][1])

print(available_cars)

print("")

separator = ', '

for (brand, modelsDict) in available_cars.items():
    print(brand)
    print("------------------")
    for (model, colorsList) in modelsDict.items():
        print(f"{model} available in {separator.join(colorsList)}")
    print("")