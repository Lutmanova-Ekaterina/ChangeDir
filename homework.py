import os

class ChangeDir:
    def __init__(self, name):
        self.name = name

    def __enter__(self):
        os.dir(self.name)

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.dir(' ')

with ChangeDir('dir1'):
    print(os.listdir())

with ChangeDir('dir2'):
    print(os.listdir())

# вывод в консоль