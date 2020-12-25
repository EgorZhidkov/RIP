# field

goods = [{'title': 'Ковер', 'price': 2000, 'color': 'green'},
         {'title': 'Диван', 'color': 'black'}]

#field(goods, 'title')

def field(items, *args):
    assert len(args) > 0
    for i in range (len(items)):

        for j in range (len(args)):
            n = args[j]
            print((items[i]).get(n,'Не обозначено'), end=' ')
        print('')

field(goods, 'title')
print(20*'-')
field(goods, 'title', 'price')
print(20*'-')
field(goods, 'title', 'price', 'color')
print(20*'-')