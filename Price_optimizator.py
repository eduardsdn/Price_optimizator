
def read_data_store(file_path): #reads pricelist.txt
    pricelist = {}
    data = []
    with open(file_path, "r") as f:
        f.readline()
        for line in f:
            parts = line.split(",")
            row = [parts[0], parts[1],int(parts[2])]

            data.append(row)
    return data