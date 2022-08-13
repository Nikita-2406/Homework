def ingredient(f):
    count = 0
    chek = 0
    book = f.readlines()
    cook_book = {}
    f.seek(0)
    for elem in book:
        elem = elem.strip('\n')
        if count == 0 and chek != 1:
            cook_book[elem] = []
            name = elem
            chek = 1
        elif count != 0 and chek == 1:
            string = elem.split('|')
            cook_book[name].append({'ingredient_name': string[0], 'quantity': int(string[1]), 'measure': string[2]})
            count -= 1
            if count == 0:
                chek = 0
        elif  chek == 1:
            count = int(elem)
    return cook_book
def get_shop_list_by_dishes(dishes, persons):
    dict_ingredients = {}
    for dish in dishes:
        for ingr in cook_book[dish]:
            dict_ingredients.setdefault(ingr['ingredient_name'], {'measure': ingr['measure'], 'quantity': 0})
            dict_ingredients[ingr['ingredient_name']]['measure'] = ingr['measure']
            dict_ingredients[ingr['ingredient_name']]['quantity'] += ingr['quantity'] * 2
    return dict_ingredients
with open('cooking_book.txt', encoding="utf-8") as f:
    cook_book = ingredient(f)
    print(cook_book)
    dict_ingredients = (get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))
    print(dict_ingredients)
    f.close()