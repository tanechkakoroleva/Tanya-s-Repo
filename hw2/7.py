num = int(input())
a = num // 1000          
b = (num // 100) % 10    
c = (num // 10) % 10     
d = num % 10             
if a == d and b == c:
    print("настоящее")
else:
    print("кривое")
