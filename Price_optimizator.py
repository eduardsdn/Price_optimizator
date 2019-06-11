import csv
import json
import math

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


document0 = get_document0('Pricelist.csv')
document1 = get_document1('Price_optimizatorG_M.video.json', "M.video", "Games_Soft_&_Entertainment", "Games_for_PS4")
document2 = get_document2('PSStore_saleG.json', "PlayStationStore", "Games", "PS4")


print('-' * 70)
print('These items are missing in your shop, but they are sold in others:')
print("↓" * 70)
print(*set(document1) - set(document0), sep='\n')
print(*set(document2) - set(document0), sep='\n')    
print('-' * 70)

less = {}
more = {}
def average_of_2_sites(document0, document1, document2):
    less = {}
    more = {}
    for name in set(document1).union(document2):
        total_sum = 0
        number_same_items = 0
        if name in document1:
            total_sum += document1[name]
            number_same_items += 1
        if name in document2:
            total_sum += document2[name]
            number_same_items += 1 
        avg = total_sum // number_same_items
        if name in document0:
            if  avg - document0[name] >= 400:
                more[name] = avg
            elif avg - document0[name] <= -400:
                less[name] = avg
        
        

    print('Avg is less: ')
    for name, avg in less.items():
        print(f'Name: {name} Price: {document0[name]} Average price: {avg}')
    print('-' * 70)
    print('Avg is more')
    for name, avg in more.items():
        print(f'Name: {name} Price {document0[name]} Average price: {avg}')
    


print(average_of_2_sites(document0, document1, document2))



