cell = input()

cols = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8}

col = cols[cell[0]]
row = int(cell[1])

if (col + row) % 2 == 0:
    print("черный")
else:
    print("белый") 
