
q = int(input('ввести желаемое количество билетов для покупки: '))

age = int(input('введите ваш возраст: '))

price1 = 990
price2 = 1390

if age < 18:
    print('проход на конференцию бесплатный!')

elif 18 <= age < 25:
    print('цена билета: ', float(price1), 'рублей')
    if q <= 3:
        print('общая стоимость: ', float(price1) * q, 'рублей')

    if q > 3:
        print('общая стоимость со скидкой 10%: ', (float(price1) * q) - (float(price1) * q / 100 * 10), 'рублей')


elif 25 <= age <= 95:
    print('цена билета: ', float(price2), 'рублей')
    if q <= 3:
        print('общая стоимость: ', float(price2) * q, 'рублей')

    if q > 3:
        print('общая стоимость со скидкой 10%: ', float(price2) * q - float(price2) * q / 100 * 10, 'рублей')

else:
    var = age > 95
    print('введите корректный возраст')
