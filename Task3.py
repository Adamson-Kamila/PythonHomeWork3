dns = []

count = int(input('Введите количество наименований: '))

for i in range(count):
    product = input('Введите наименование товара: ')
    price = int(input('Введите цену товара: '))
    quantity = int(input('Введите количество товара: '))
    measure = input('Введите единицу измерения товара: ')

    store = {'название': product, 'цена': price, 'количество': quantity, 'ед': measure}
    key = (i + 1, store)
    dns.append(key)

print(dns)

new_store = {'название': [], 'цена': [], 'количество': [], 'ед': []}
arr_name = []
arr_price = []
arr_quantity = []
arr_measure = []
for i in range(count):
    arr_name.append(dns[i][1]['название'])
    new_store['название'] = arr_name

    arr_price.append(dns[i][1]['цена'])
    new_store['цена'] = arr_price

    arr_quantity.append(dns[i][1]['количество'])
    new_store['количество'] = arr_quantity

    arr_measure.append(dns[i][1]['ед'])
    new_store['ед'] = arr_measure

print(new_store)