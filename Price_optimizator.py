import csv
import json


def get_document0(file_name):
    document0 = {}
    with open (file_name, 'r', encoding='utf-8') as f:
        for line in f.read().split('\n')[1:]:
            parts = line.split(',')
            document0[parts[1]] = int(parts[2])
    return document0


def get_document1(file_name, catalog1, catalog2, catalog3):
    document1 = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        for item in data[catalog1][catalog2][catalog3]:
            document1[item['name']] = item['price']
    return document1


def get_document2(file_name, catalog1, catalog2, catalog3):
    document2 = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        for item in data[catalog1][catalog2][catalog3]:
            document2[item['name']] = item['price']
    return document2


def get_document3(file_name, catalog1, catalog2, catalog3):
    document3 = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        for item in data[catalog1][catalog2][catalog3]:
            document3[item['name']] = item['price']
    return document3


def get_document4(file_name, catalog1, catalog2, catalog3):
    document4 = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        for item in data[catalog1][catalog2][catalog3]:
            document4[item['name']] = item['price']
    return document4

def get_document5(file_name, catalog1, catalog2, catalog3, catalog4, catalog5):
    document5 = {}
    with open(file_name, 'r', encoding='utf-8') as f:
       data = json.loads(f.read())
       for item in data[catalog1][catalog2][catalog3][catalog4][catalog5]:
            document5[item['name']] = item['price']
    return document5
        

document0 = get_document0('Pricelist.csv')
document1 = get_document1('Price_optimizatorG_M.video.json', "M.video", "Games_Soft_&_Entertainment", "Games_for_PS4")
document2 = get_document2('PSStore_saleG.json', "PlayStationStore", "Games", "PS4")
document3 = get_document3('Game_Park.json', "Game_Park_main_page", "PlayStation_4", "Games")
document4 = get_document4('1C_Interest.json', "1C_Interest", "Games_&_Consols", "Playstation_4")
document5 = get_document5('DNS.json', "DNS", "Games_&_Consols", "Entertainment", "Videogames", "PS4")


def average_of_2_sites(document0, document1, document2, document3, document4, document5):
    a = int(input("Enter a higher boundary: "))
    b = int(input("Enter a lower boundary: "))
    print('These items are missing in your shop, but they are sold in others:')
    print("↓" * 80)
    less = {}
    more = {}
    for name in set(document1).union(document2).union(document3).union(document4).union(document5):
        total_sum = 0
        number_same_items = 0
        if name in document1:
            total_sum += document1[name]
            number_same_items += 1
        if name in document2:
            total_sum += document2[name]
            number_same_items += 1 
        if name in document3:
            total_sum += document3[name]
            number_same_items += 1 
        if name in document4:
            total_sum += document4[name]
            number_same_items += 1
        if name in document5:
            total_sum += document5[name]
            number_same_items += 1
        avg = total_sum // number_same_items
        if name in document0:
            if  avg - document0[name] >= a:
                more[name] = avg
            elif avg - document0[name] <= -b:
                less[name] = avg     
        else:
            print(f'The item: {name} is sold in {number_same_items} shop(s)')
    print('_' * 80)


    print('Avg is less: ')
    for name, avg in less.items():
        print(f'Name: {name}, Price: {document0[name]}, Average price: {avg}, Difference: {document0[name] - avg}')
    print('-' * 70)
    print('Avg is more')
    for name, avg in more.items():
        print(f'Name: {name}, Price {document0[name]}, Average price: {avg}, Difference: {avg - document0[name]}')
    


print(average_of_2_sites(document0, document1, document2, document3, document4, document5))

