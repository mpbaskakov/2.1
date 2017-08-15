with open('recipe.txt', encoding='utf8') as f:
    cook_book = {}
    list_of_ingridients = []
    dict_of_ingridients = {}
    for line in f:
        dish = line.strip()
        num_of_ingridients = int(f.readline().strip())
        for i in range(num_of_ingridients):
            ingridients = f.readline().strip()
            ingridients = ingridients.split(' | ')
            dict_of_ingridients['ingridient_name'] = ingridients[0]
            dict_of_ingridients['quantity'] = int(ingridients[1])
            dict_of_ingridients['measure'] = ingridients[2]
            list_of_ingridients.append(dict_of_ingridients)
            dict_of_ingridients = {}
        cook_book[dish] = list_of_ingridients
        list_of_ingridients = []

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            new_shop_list_item = dict(ingridient)
            new_shop_list_item['quantity'] *= person_count
            if new_shop_list_item['ingridient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingridient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingridient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print('{} {} {}'.format(shop_list_item['ingridient_name'], shop_list_item['quantity'],
                                shop_list_item['measure']))

def create_shop_list():
    person_count = int(input('Введите количество человек: '))
    dishes = input('Введите блюда в расчете на одного человека (через запятую): ') \
        .lower().split(', ')
    shop_list = get_shop_list_by_dishes(dishes, person_count)
    print_shop_list(shop_list)

create_shop_list()