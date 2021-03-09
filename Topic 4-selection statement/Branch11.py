
gross = float(input('Gross annual income: '))
deduction = float(input('Less tax deduction: '))
 #   Income = float(input('taxable income:'))
taxPaid = float(input('tax paid:'))

taxableIncome = gross - deduction
if 0 <= taxableIncome and taxableIncome < 8000:
    rate = 0
    print('Tax Rate 0% Gross')
elif 8000 <= taxableIncome < 15000:
    rate = 0.25
    print('Tax Rate 25% Gross')
elif 15000 <= taxableIncome < 25000:
    rate = 0.35
    print('tax rate 35% Gross')
elif 25000 <= taxableIncome < 50000:
    rate = 0.42
    print('tax rate 42% gross')
elif 50000 <= taxableIncome < 60000:
    rate = 0.48
    print('tax rate 48% gross')
    
print(rate)
taxPayable = taxableIncome * rate 

refund = taxPaid - taxPayable
print("refund : {}".format(refund))