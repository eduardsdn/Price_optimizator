
def get_document0(file_name):
    document0 = {}
    with open (file_name, 'r', encoding='utf-8') as f:
        for line in f.read().split('\n')[1:]:
            parts = line.split(',')
            document0[parts[1]] = int(parts[2])
    return document0