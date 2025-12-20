def gen():
    num = 0
    while True:
        yield num
        num = num + 2

def square():
    num = 1
    while True:
        yield num * num
        num += 1

even = gen()
sqr = square()

print("---Even---")

for i in range(5):
    print(next(even))

print("---Squares---")

for i in range(5):
    print(next(sqr))
