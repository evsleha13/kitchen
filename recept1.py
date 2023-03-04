
from pprint import pprint

with open('sostav1.txt', encoding='utf-8') as file:
    cook_book = {}
    for line in file:
        dish_name = line.strip()
        ingredients_count = int(file.readline())
        ingredients = []
        for _ in range(ingredients_count):
            ingr = file.readline().strip()
            ingredient_name, quantity, measure = ingr.split(' | ')
            ingredients.append(

                {'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        cook_book[dish_name] = ingredients
        file.readline()
pprint(cook_book, sort_dicts=False)


my_dishes = ['Омлет', 'Утка по-пекински', 'Запеченный картофель']
dish_list = list(cook_book.keys())
def get_shop_list_by_dishes(my_dishes, person_count):
    ingredients_list = []
    calculation_products_dict = {}
    for one_dish in my_dishes:
        if one_dish in dish_list:
            ingredients_list.append(cook_book[one_dish])
            for dish_ingredients in ingredients_list:
                for separate_ingredient in dish_ingredients:
                    i = separate_ingredient['ingredient_name']
                    m = separate_ingredient['measure']
                    q = int(separate_ingredient['quantity'])
                    # calculation_products_dict[i] = {'measure':m, 'quantity':q * person_count}
                    if i in calculation_products_dict.keys():
                        q += int(separate_ingredient['quantity'])
                        calculation_products_dict[i] = {'measure':m, 'quantity':q * person_count}
                    else:
                        calculation_products_dict[i] = {'measure':m, 'quantity':q * person_count}

    return calculation_products_dict

pprint(get_shop_list_by_dishes(my_dishes, 1))
