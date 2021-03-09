while True:
    num = input('tell the income: ')
    if not num.isdigit():
        break
    num = int(num)
    if 0 <= num < 8000:
        print('Tax Rate 0% Gross')
    elif 8000 <= num < 15000:
        print('Tax Rate 25% Gross')
    elif 15000 <= num < 25000:
        print('tax rate 35% Gross')
    elif 25000 <= num < 50000:
        print('tax rate 42% gross')
    elif 50000 <= num < 60000:
        print('tax rate 48% gross')
    