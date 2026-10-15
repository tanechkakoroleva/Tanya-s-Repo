import math
n = int(input())
c = int(input())
number = int(input())
page = math.ceil((number / (n * c)))
column = math.ceil((number % (n * c)) / n)
string = (number % (n * c)) % n
print("страница", page, "столбец", column, "строка", string)
