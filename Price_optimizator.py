import csv
import json


def get_document0(file_name):
    document0 = {}
    with open (file_name, 'r', encoding='utf-8') as f:
        for line in f.read().split('\n')[1:]:
            parts = line.split(',')
            document0[parts[1]] = int(parts[2])
    return document0


def get_document(file_name, *path):
    document = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        data = json.loads(f.read())
        for key in path:
            data = data[key]
        for item in data:
            document[item['name']] = item['price']
    return document

        
document0 = get_document0('Pricelist.csv')
docs = [
    get_document('Price_optimizatorG_M.video.json', "M.video", "Games_Soft_&_Entertainment", "Games_for_PS4"),
    get_document('PSStore_saleG.json', "PlayStationStore", "Games", "PS4"),
    get_document('Game_Park.json', "Game_Park_main_page", "PlayStation_4", "Games"),
    get_document('1C_Interest.json', "1C_Interest", "Games_&_Consols", "Playstation_4"),
    get_document('DNS.json', "DNS", "Games_&_Consols", "Entertainment", "Videogames", "PS4")
]

def average_of_2_sites(document0, *docs):
    with open('output.txt', 'w', encoding='utf-8') as f:
        a = int(input("Enter a higher boundary: "))
        b = int(input("Enter a lower boundary: "))
        f.write('These items are missing in your shop, but they are sold in others:\n')
        f.write("↓" * 80 + '\n')
        less = {}
        more = {}
        for name in set().union(*docs):
            total_sum = 0
            number_same_items = 0
            for doc in docs:
                if name in doc:
                    total_sum += doc[name]
                    number_same_items += 1
            avg = total_sum // number_same_items
            if name in document0:
                if  avg - document0[name] >= a:
                    more[name] = avg
                elif avg - document0[name] <= -b:
                    less[name] = avg     
            else:
                f.write(f'The item: {name} is sold in {number_same_items} shop(s)\n')
        f.write('_' * 80 + '\n')


        f.write('Avg is less:\n')
        for name, avg in less.items():
            f.write(f'Name: {name}, Price: {document0[name]}, Average price: {avg}, Difference: {document0[name] - avg}\n')
        f.write('_' * 70 + '\n')
        f.write('Avg is more\n')
        for name, avg in more.items():
            f.write(f'Name: {name}, Price {document0[name]}, Average price: {avg}, Difference: {avg - document0[name]}\n')
    


average_of_2_sites(document0, *docs)
