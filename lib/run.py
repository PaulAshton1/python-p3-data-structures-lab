from lib.data_structures import *

print(get_names(spicy_foods))
print(get_spiciest_foods(spicy_foods))
print_spicy_foods(spicy_foods)
print(get_spicy_food_by_cuisine(spicy_foods, "American"))
print_spiciest_foods(spicy_foods)
print(average_heat_level(spicy_foods))

new_food = {
    "name": "Griot",
    "cuisine": "Haitian",
    "heat_level": 10,
}
print(create_spicy_food(spicy_foods, new_food))
