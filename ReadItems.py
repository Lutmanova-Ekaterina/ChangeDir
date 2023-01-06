import csv

class ReadItems:
    def __init__(self, file, mode):
        self.file = file
        self.mode = mode

    def __enter__(self):
        self.f = open(self.file, self.mode)
        self.result = csv.DictReader(self, f)
        return self.result

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.f.close()

def show_items(file):
    with ReadItems(file, 'r') as items:
        for item in items:
            print(item)

show_items('items.csv')

# вывод в консоль
