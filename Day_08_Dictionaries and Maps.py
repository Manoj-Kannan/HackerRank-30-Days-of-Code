n = int(input())
book = dict()

for i in range(n):
    contact = input().split()
    book.update({contact[0]:contact[1]})

while True:
    try:
        name = input()
        if name in book:
            print('{}={}'.format(name,book[name]))
        else:
            print('Not found')
    except:
        break
